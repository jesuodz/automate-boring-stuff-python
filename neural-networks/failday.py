import numpy as np

def sig(x):
    """Función sigmoidal"""
    return 1.0 / (1 + np.exp(-x))

def sig_der(x):
    """Derivada de la función sigmoidal"""
    return x * (1.0 - x)

class Network:
    def __init__(self, input, y, bias, learning_rate):
        self.input = input
        self.y = y
        self.bias = bias
        self.lr = learning_rate
        self.w1 = np.random.rand(self.input.shape[1], 2)
        self.w2 = np.random.rand(2, 3)
        self.w3 = np.random.rand(3, 1)
        self.output = np.zeros(self.y.shape)

    def feedforward(self):
        self.layer1 = sig(np.dot(self.input, self.w1) + self.bias)
        self.layer2 = sig(np.dot(self.layer1, self.w2) + self.bias)
        self.output = sig(np.dot(self.layer2, self.w3) + self.bias)

    def backprop(self):
        """Algoritmo de propagación hacia atrás (backpropagation)"""
        
        # Calcula los costes de w3 partiendo de la der. de output
        dcost = 2 * (self.output - self.y)
        d_w3 = np.dot(self.layer2.T, dcost * sig_der(self.output))

        # Calcula los costes de w2 partiendo de la der. de layer2
        d_layer2 = np.dot(dcost * sig_der(self.output), self.w3.T) * sig_der(self.layer2)
        d_w2 = np.dot(self.layer1.T, d_layer2)
        
        # Calcula los costes de w1 partiendo de la der. de layer1
        d_layer1 = np.dot(d_layer2, self.w2.T) * sig_der(self.layer1)
        d_w1 = np.dot(self.input.T, d_layer1)

        # Actualiza los pesos
        self.w3 -= self.lr * d_w3
        self.w2 -= self.lr * d_w2
        self.w1 -= self.lr * d_w1

    def compute(self, arr):
        data = np.array(arr)
        l1 = sig(np.dot(data, self.w1) + self.bias)
        l2 = sig(np.dot(l1, self.w2) + self.bias)

        return sig( np.dot(l2, self.w3) + self.bias )

if __name__ == "__main__":
    np.random.seed(100)         # Qué hace?
    bias = np.random.rand(1)    # Qué significa?
    learning_rate = 0.05        # Para qué sirve?

    feature_set = np.array([[0,1,0],
                            [0,0,1],
                            [1,0,1],
                            [0,0,0]])
    expected = np.array([[1,0,0,0]]).reshape(4,1)

    nn = Network(feature_set, expected, bias, learning_rate)

    for epoch in range(1500):
        nn.feedforward()
        nn.backprop()

    # print(nn.compute([0,0,0,0]))    # aprox. 0...
    # print(nn.compute([1,1,1,1]))    # aprox. 1...
    # print(nn.compute([0,1,1,0]))    # aprox. 1...
    # print(nn.output)    
    print(2 * (nn.output - nn.y) * sig_der(nn.output))