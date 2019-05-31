import numpy as np

def heavyside(c):
    # funcion signo
    if c < 0:
        return 0
    return 1

class Neuron:
    def __init__(self, x, umbral):
        self.input      = x
        self.u          = umbral
        self.weights    = np.full(self.input.shape[1], 0.5)
        self.output     = np.zeros(self.input.shape[0])

    def calc(self):
        cross_mult = np.dot(self.input, self.weights) - self.u
        self.output = list(map(heavyside, cross_mult))

X = np.array([[1,1], [0,1], [0,0], [1,0]])
n = Neuron(X, 0.75)
n.calc()
print(n.output)
