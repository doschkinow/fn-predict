import os
from tensorflow import keras
import numpy as np
from skimage import io
from skimage import transform
from skimage.transform import rescale

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

model = keras.models.load_model('digit_model.h5')

img = io.imread('/tmp/image.jpg', as_gray=True)
img = rescale(img, 28/400,anti_aliasing=True, multichannel=False, mode='reflect')

# Add the image to a batch where it's the only member.
img = (np.expand_dims(img,0))

# predict the image
prediction = model.predict(img)
probabilities = prediction[0].tolist()

print(np.argmax(prediction[0]), end=' ')
for i in probabilities[1:]:
    print("%7.5f" % i, end=' ')
print("%7.5f"% probabilities[0], end='')

