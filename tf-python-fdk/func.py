import io
import os
import sys
import base64
from tensorflow import keras
import numpy as np
from skimage import io as skimageio
from skimage import transform
from skimage import color
from skimage.transform import rescale
import fdk
from fdk import response

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

model = keras.models.load_model('digit_model.h5')

def handler(ctx, data: io.BytesIO=None):
    encoded_image = data.read().decode("utf-8")
    img_data = base64.b64decode(encoded_image)
    img = skimageio.imread(img_data, plugin='imageio')
    img = color.rgb2gray(img)
    img = rescale(img, 28 / 400, anti_aliasing=True, multichannel=False, mode='reflect')
    # Add the image to a batch where it's the only member.
    img = (np.expand_dims(img, 0))
    # predict the digit in the image
    prediction = model.predict(img)
    probabilities = prediction[0].tolist()
    probabilities = probabilities[1:] + probabilities[0:1]
    sprobabilities = (' '.join(['%7.5f']*len(probabilities)))%tuple(probabilities)
    result = str(np.argmax(prediction[0])) + ' ' + sprobabilities
#   return result
    return response.Response(
        ctx, response_data=result,
        status_code=200,
        headers={"Access-Control-Allow-Origin":"*"}
    )
