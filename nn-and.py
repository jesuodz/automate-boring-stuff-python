import random

def bth(x):
    """Binary Threshold function"""
    return x * 0

class NeuralNetwork:
    def __init__(self, x, y):
        self.input  = x
        self.w1     = self.input[0] * random.random()
        self.w2     = self.input[1] * random.random()
        self.y      = y

    def feedforward(self):
        self.layer = self.w1 + self.w2
        print("Layer:",self.layer)
        self.output = bth(self.layer)

if __name__ == "__main__":
    X = [1, 1]
    y = 1
    nn = NeuralNetwork(X, y)

    nn.feedforward()
    print(nn.output)
    print(nn.w1,nn.w2)
