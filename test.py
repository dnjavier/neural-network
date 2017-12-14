from perceptron import Perceptron

#three inputs
p = Perceptron(3)
p.inputs[0] = 255
p.inputs[1] = 255
p.inputs[2] = 255

guess = p.feedForward()
print guess