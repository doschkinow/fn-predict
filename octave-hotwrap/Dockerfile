FROM delabassee/hotwrap:latest as hotwrap

FROM parallelworks/octave:v4.0.0_rootuser
ADD fn-predict /mnt/fn-predict
WORKDIR /mnt/fn-predict
CMD ["/bin/bash", "predict_image.sh"]

#Install hotwrap binary in your container
COPY --from=hotwrap /hotwrap /hotwrap
ENTRYPOINT ["/hotwrap"]
