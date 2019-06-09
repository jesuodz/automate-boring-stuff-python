import numpy as np

def heavyside(n):
    """ funcion signo """
    if n < 0:
        return 1
    else:
        return 0

class Neuron:
    def __init__(self, x, umbral):
        self.input      = x
        self.u          = umbral
        self.weights1   = np.full((self.input.shape[1], 2), 0.5)
        self.weights2   = np.full(self.input.shape[1], 0.5)
        self.output     = np.zeros(self.input.shape[1])

    def feedforward(self):
        """ Calcula la salida """

        # Determina el coste para la capa1
        cost = np.dot(self.input, self.weights1) - self.u
        print(cost)
        # Aplica f(x) para casa suma del coste
        l1 = [[n,n] for n in map(heavyside, cost.sum(axis=1))]
        print(l1)
        cost_l1 = np.dot(l1, self.weights2) - self.u
        self.output = list(map(heavyside, cost_l1))

# Esperado: [0, 1, 0, 1]
X = np.array([[1,1], [0,1], [0,0], [1,0]])
n = Neuron(X, 0.75)
n.feedforward()
print(n.output)
