# read base64 encoded image from stdin
#
# output prediction digit and digit probabilities on stdout

base64 -d >/tmp/image.jpg
octave --silent --no-window-system --no-history predict_image.m
