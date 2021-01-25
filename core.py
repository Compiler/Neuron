#feed forward perceptron model

import numpy as np

inputs = [[1, 2, 3, 4], 
            [1, 2, 3, 4], 
            [1, 2, 3, 4]]

weights = [ [3.1, 1.2, 4.2, 5.1],
            [1.2, 2.3, 3.4, 4.5],
            [3.2, 5.4, 2.3, 1.2]]
bias = [1, 1.5, 2]

output = np.dot(inputs, np.array(weights).T) + bias

print(output)