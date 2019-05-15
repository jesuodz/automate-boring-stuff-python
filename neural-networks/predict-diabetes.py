import numpy as np

def sigmoid(x):
    return 1.0 / (1 + np.exp(-x))

def sigmoid_der(x):
    return 1 * (1.0 - x)

class NeuralNetwork:
    def __init__(self, input, predicted, bias, learning_rate):
        self.input = input
        self.weights = np.random.rand(self.input.shape[1], 1)
        self.predicted = predicted
        self.b = bias
        self.lr = learning_rate
        self.output = np.zeros(self.predicted.shape)

    def feedforward(self):
        # Paso 1:
        # Producto entre las entradas y los pesos, más la presunción.
        XW = np.dot(self.input, self.weights) + self.b

        # Paso 2:
        # Salida, resultado de pasar X.W a través de la función Sig.
        self.output = sigmoid( XW )

    def backprop(self):
        # Paso 1:
        # Encuentra el error
        self.error = self.output - self.predicted

        # Paso 2:
        # 
        self.dcost_dpred = self.error
        self.dpred_doutput = sigmoid_der( sigmoid(self.output) )

        self.output_delta = self.dcost_dpred * self.dpred_doutput

        inv_input = self.input.T
        self.weights -= self.lr * np.dot(inv_input, self.output_delta)

        for n in self.output_delta:
            self.b -= self.lr * n

    def result(self, data):

        self.data = np.array(data)

        return sigmoid( np.dot(self.data, self.weights) + self.b )

if __name__ == "__main__":
    np.random.seed(42)
    bias = np.random.rand(1)
    learning_rate = 0.05

    feature_set = np.array([[0,1,0],
                            [0,0,0],
                            [0,0,1],
                            [1,0,0],
                            [1,1,0],
                            [0,1,1],
                            [1,1,1],
                            [1,0,1]])
    predicted = np.array([[1,0,0,0,1,1,1,0]]).reshape(8, 1)

    nn = NeuralNetwork(feature_set, predicted, bias, learning_rate)

    for epoch in range(20000):
        nn.feedforward()
        nn.backprop()

    print(nn.result([1,1,0,1]))
    print(nn.result([0,1,0,1]))
    