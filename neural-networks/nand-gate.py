import numpy as np

def heavyside(n):
    """ funcion signo """
    return 1 if n < 0 else 0

class Neuron:
    def __init__(self, x, umbral):
        self.input      = x
        self.u          = umbral
        self.weights    = np.full(self.input.shape[1], 0.5)
        self.output     = np.zeros(self.input.shape[1])

    def feedforward(self):
        """ Calcula la salida """
        cost = np.dot(self.input, self.weights) - self.u
        self.output = list(map(heavyside, cost))

# Esperado: [0, 1, 1, 1]
X = np.array([[1,1], [0,1], [0,0], [1,0]])
n = Neuron(X, 0.75)
n.feedforward()
print(n.output)
