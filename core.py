#feed forward perceptron model

import numpy as np
np.random.seed(0)

inputs = [[1, 2, 3, 4], 
            [4,3, 2, 1], 
            [4, 2, 2, 4]]

class Layer:
    def __init__(self, inputCount, neuronCount):
        self.weights = 0.1* np.random.randn(inputCount, neuronCount)
        self.biases = 0.0001 * np.random.randn(1, neuronCount)
        self.outputs = []
    def forward(self, inputs):
        self.outputs = np.dot(inputs, self.weights) + self.biases

layer1 = Layer(4, 3)
layer2 = Layer(3, 3)
layer1.forward(inputs)
layer2.forward(layer1.outputs)
print(layer1.outputs)