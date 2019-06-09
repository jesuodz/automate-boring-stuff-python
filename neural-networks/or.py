import numpy as np

def sigmoid(n):
    return 1.0 / (1 + np.exp(-n))

class NeuralNetwork:
    def __init__(self, x, y):
        self.input      = x
        self.weights    = np.random.rand(self.input.shape[1],2)
        self.y          = y
        self.output     = np.zeros(y.shape)

    def feedforward(self):
        self.output = np.sum(sigmoid(np.dot(self.input, self.weights)))

if __name__ == "__main__":
    X1 = np.array([[1, 1]])
    X2 = np.array([[0, 1]])
    X3 = np.array([[1, 0]])
    X4 = np.array([[0, 0]])
    y = np.array([[0]])

    test1 = NeuralNetwork(X1, y)
    test2 = NeuralNetwork(X2, y)
    test3 = NeuralNetwork(X3, y)
    test4 = NeuralNetwork(X4, y)


    test1.feedforward()
    test2.feedforward()
    test3.feedforward()
    test4.feedforward()

    # if output > 1.0 : output is True else output is False
    print([test1.output,
           test2.output,
           test3.output,
           test4.output])
