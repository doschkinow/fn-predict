this project packs machine learning models in docker containers to be exposed as fn functions (see serverless project fn) and used to predict the digit on a digit image.

The models are trained using octave (20x20 gray digit image examples) and tensorflow (28x28 gray digit image examples).
The containers expect a 400x400 base64 encoded digit image on stdin and output the predicted digit and the corresponding probabilities for the digits 1-9 and 0.

Examples:

[pdos@ol7 fn-predict]$ ls

fünf-base64-encoded.txt  octave  sechs-base64-encoded.txt  tensorflow

[pdos@ol7 fn-predict]$ cat fünf-base64-encoded.txt |docker run --rm -i doschkinow/fn-predict-octave:1.0

5 0.00030 0.00000 0.19404 0.00640 0.73716 0.00006 0.00131 0.00390 0.00221 0.00694
[pdos@ol7 fn-predict]$ 
[pdos@ol7 fn-predict]$ cat fünf-base64-encoded.txt |docker run --rm -i doschkinow/fn-predict-tf:1.0
5 0.06711 0.05290 0.12172 0.03847 0.40147 0.04575 0.05587 0.07002 0.10527 0.04143
[pdos@ol7 fn-predict]$ 
[pdos@ol7 fn-predict]$ cat sechs-base64-encoded.txt |docker run --rm -i doschkinow/fn-predict-octave:1.0
6 0.00049 0.00869 0.00088 0.00114 0.18942 0.59728 0.00003 0.02711 0.00049 0.01952
[pdos@ol7 fn-predict]$ 
[pdos@ol7 fn-predict]$ cat sechs-base64-encoded.txt |docker run --rm -i doschkinow/fn-predict-tf:1.0
6 0.04501 0.06740 0.05263 0.08043 0.15762 0.25701 0.04532 0.16817 0.04600 0.08041
[pdos@ol7 fn-predict]$ 
[pdos@ol7 fn-predict]$