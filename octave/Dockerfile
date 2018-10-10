# to build:
# docker build -t <tag> .
# e.g.: docker build -t doschkinow/fn-predict-octave:1.0 .
#
#
# to test
# cat <base64-encoded-image> | docker run -i --rm <container-from-this-image>
# e.g.: cat fn-predict/two-base64-encoded.txt | docker run --rm -i doschkinow/fn-predict-octave:1.0
# this should return a prediction digit and probabilities for all digits

FROM openmicroscopy/octave

ADD fn-predict /mnt/fn-predict
WORKDIR /mnt/fn-predict
ENTRYPOINT ["/bin/bash", "./predict_image.sh"]
