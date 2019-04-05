warning('off', 'Octave:GraphicsMagic-Quantum-Depth');
#
# load learned model parameters Theta1, Theta2
#
load('digit_model.mat');
#
# convert jpg image to a gray 20x20 representation
#
vectorImage = imageTo20x20Gray('/tmp/image.jpg');
#
# predict digit
#
predict(Theta1, Theta2, vectorImage);
