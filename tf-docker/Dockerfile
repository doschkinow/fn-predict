FROM tensorflow/tensorflow:1.10.1-py3

RUN pip install scikit-image && pip install imageio && pip install rpyc

ADD fn-predict /mnt/fn-predict
WORKDIR /mnt/fn-predict
CMD ["/bin/bash", "predict_image.sh"]
