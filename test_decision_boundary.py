import numpy as np
data = np.random.rand(10, 2)                 # 10 rows, 2 columns, random value
labels = np.random.randint(2, size=(10, 1))  # 10 rows, 1 column, random 1 or 0

def my_classification_function(x):
    return (x[:, 0] + x[:, 1] > 1).astype(int).reshape(-1, 1)

import decision_boundary
decision_boundary.plot(data, labels, lambda x: my_classification_function(x), resolution=50, padding_percent=80)
