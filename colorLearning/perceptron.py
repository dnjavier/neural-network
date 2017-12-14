import random

class Perceptron:
    # learning constant
    C = 0.008

    # arrays that hold inputs and weights
    inputs
    weights

    # qty of inputs
    n

    def __init__(self, ninputs):
        self.n = ninputs
        self.inputs = []
        self.weights = []

        #bias
        self.inputs[self.n - 1] = 1

        for i in range(0, self.n):
            #The weights are picked randomly to start.
            # a trick to get values from -1 to 1
            self.weights[i] = random.uniform(-1000, 1000) / 1000

    #reset weights to random values
    def randomize():
        global n
        global weights
        for i in range(0, n):
            #The weights are picked randomly to start.
            # a trick to get values from -1 to 1
            weights[i] = random.uniform(-1000, 1000) / 1000

    # training function
    def train(desired, guess):
        global n
        global weights
        global inputs
        global c
        error = desired - guess

        for i in range(0, n):
            weights[i] += c * error * inputs[i]

    def feedForward():
        global inputs
        global weights
        sum = 0
        for i in range(0, n):
            sum += inputs[i] * weights[i]
        
        return __activate(sum)

    def weightedSum():
        sum = 0
        for i in range(0, n):
            sum += inputs[i] * weights[i]
        
        return sum

    def __activate(sum):
        if sum > 0:
            return 1
        else:
            return -1