this project packs machine learning models in docker containers to be exposed as fn functions (see serverless project fn) 
to predict the digit on a 400x400 base64-encoded digit image.

The models are trained using GNU Octave (5000 20x20 gray digit image examples on a Neural Network with 1 hidden layer with 25 units) and 
Tensorflow (MNIST 28x28 gray digit image examples on a Neural Network with 1 hidden layer with 512 units).

The containers expect a 400x400 base64 encoded digit image on stdin and output the predicted digit and the corresponding probabilities 
for the digits 1-9 and 0.

The folders octave-docker and tf-docker contain the Dockerfile for building the corresponding containers. 

To test octave-docker:

cd octave-docker
docker build -t octave-docker .
cat ../vier-base64-encoded.txt |docker run -i octave-docker

result: 
4 0.00519 0.00069 0.02413 0.96044 0.01314 0.00080 0.00100 0.00118 0.06225 0.00000

To test tf-docker:

cd tf-docker
docker build -t tf-docker .
cat ../vier-base64-encoded.txt |docker run -i tf-docker

result: 
4 0.06309 0.07452 0.04057 0.34499 0.13020 0.05446 0.08988 0.08099 0.09358 0.02772

The folders octave-hotwrap and tf-hotwrap show how above containers can be exposed as Fn functions using 
Fn hotwrap(https://github.com/fnproject/hotwrap)

To test octave-hotwrap:

cd octave-hotwrap
fn -v deploy --no-bump --app predict --local
curl -d `cat ../vier-base64-encoded.txt` http://localhost:8080/t/predict/octave-hotwrap

result: 
4 0.00519 0.00069 0.02413 0.96044 0.01314 0.00080 0.00100 0.00118 0.06225 0.00000

To test tf-hotwrap:

cd tf-hotwrap
fn -v deploy --no-bump --app predict --local
curl -d `cat ../vier-base64-encoded.txt` http://localhost:8080/t/predict/tf-hotwrap

result: 
4 0.06309 0.07452 0.04057 0.34499 0.13020 0.05446 0.08988 0.08099 0.09358 0.02772

The folder tf-python-fdk shows how the tensorflow code used in the tf docker container can be rewritten
to use the Fn Python FDK. With this implementation, hot functions are very fast since they execute only the function call back and
the time to start the function container and to execute the python initialization code is saved.

To test tf-python-fdk:
cd tf-python-fdk
time curl -d `cat ../vier-base64-encoded.txt` http://localhost:8080/t/predict/tf-python-fdk

result (cold function call, if called first time):
4 0.06309 0.07452 0.04057 0.34499 0.13020 0.05446 0.08988 0.08099 0.09358 0.02772
real	0m18.829s
user	0m0.005s
sys	0m0.012s

result (hot function call, if called within 30s from last one):
4 0.06309 0.07452 0.04057 0.34499 0.13020 0.05446 0.08988 0.08099 0.09358 0.02772
real	0m0.190s
user	0m0.003s
sys	0m0.010s

