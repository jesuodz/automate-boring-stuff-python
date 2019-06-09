#! python3
import numpy as np

def heavyside(x):
    return 1

class NeuralNetwork:
    def __init__(self, x):
        self.input = x
        self.weights1 = np.random.rand(self.input.shape[1], 2)
        self.weights2 = np.random.rand(2, 1)
        self.output = np.zeros(x.shape)

    def feedforward(self):
        self.layer1 = heavyside(np.dot(self.input, np.sum(self.weights1)))
        # self.output = heavyside(np.dot(self.layer1, self.weights2))

if __name__ == '__main__':
    X = np.array([[0, 1]])

    nn = NeuralNetwork(X)
    
    nn.feedforward()

    print(nn.weights1.shape)
