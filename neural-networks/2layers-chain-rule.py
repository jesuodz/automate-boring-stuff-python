import numpy as np

def sig(x):
    return 1 / (1 + np.exp(-x))

def sig_der(x):
    return sig(x) * (1 - sig(x))

class NeuralNetwork:
    def __init__(self, input, y, bias, learning_rate=0):
        self.input = input
        self.y = y
        self.wh = np.random.rand(self.input.shape[1],2)
        self.wo = np.random.rand(2, 1)
        self.bias = bias
        self.lr = learning_rate
        self.ao = np.zeros(self.y.shape)

    def feedforward(self):

        # z(x) --> activación
        # a(x) --> funcion de activacion aplicada a z(x)
        self.zh = np.dot(self.input, self.wh) + self.bias
        self.zo = np.dot(self.zh, self.wo) + self.bias

        self.ah = sig(self.zh)
        self.ao = sig(self.zo)

    def backprop(self):
        # Función de coste
        cost = self.ao - self.y

        # Regla de la cadena para derivar el costo respecto a wo
        # dcost * dao * dzo
        dcost = 2 * cost
        dao = sig_der(self.zo)
        dzo = self.input.T

        dwo = np.dot(dzo, dcost * dao)

        # Regla de la cadena para derivar el costo respecto a wh
        # 

        # Actualiza los pesos        
        self.wo -= dwo

        # self.wo -= self.lr * dwo

        # for n in del_output:
        #     self.bias -= self.lr * n

if __name__ == '__main__':
    bias = np.random.rand(1)

    feature_set = np.array([[0,0,0],
                            [0,1,0],
                            [1,0,1],
                            [0,0,1]])
    expected = np.array([[0,1,0,0]]).reshape(4,1)

    nn = NeuralNetwork(feature_set, expected, bias)

    for epoch in range(1500):
        nn.feedforward()
        nn.backprop()

    # print(nn.output)
    print(nn.ao)