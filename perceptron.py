import random

class Perceptron:
    global activate
    # learning constant
    C = 0.008

    # arrays that hold inputs and weights
    inputs = []
    weights = []

    # qty of inputs
    n = 0

    def __init__(self, ninputs):
        self.n = ninputs + 1 #one more for bias
        self.inputs = [0] * self.n
        self.weights = [0] * self.n
        
        #bias
        self.inputs[self.n - 1] = 1
        self.randomize()

    #reset weights to random values
    def randomize(self):
        for i in range(0, self.n):
            #The weights are picked randomly to start.
            # a trick to get values from -1 to 1
            self.weights[i] = random.uniform(-1000, 1000) / 1000

    # training function
    def train(self, desired, guess):
        error = desired - guess

        for i in range(0, self.n):
            self.weights[i] += self.C * error * self.inputs[i]

    def feedForward(self):
        sum = 0
        for i in range(0, self.n):
            sum += self.inputs[i] * self.weights[i]
        
        return activate(sum)

    def activate(sum):
        return 1 if sum > 0 else -1
