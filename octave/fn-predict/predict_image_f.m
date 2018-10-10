function p = predict_image(jpg)
warning('off', 'Octave:GraphicsMagic-Quantum-Depth');
load('ex4weights.mat');
vectorImage = imageTo20x20Gray(jpg);
displayData(vectorImage);
predict(Theta1, Theta2, vectorImage);
end