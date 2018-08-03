# decision-boundary

A minimalist Python package to draw 2D decision boundaries in machine learning

## Prerequisites

You need your data as two NumPy matrices: a collection of 2D points, and a collection of binary labels.

    import numpy as np
    x = np.random.rand(10, 2)               # matrix of (N, 2), random value
    y = np.random.randint(2, size=(10, 1))  # matrix of (N, 1), elements randomly 0 or 1

Then you need a classification function that takes a matrix of 2D points and returns a matrix of labels:

    def my_classification_function(points):                        # points is a matrix of (N, 2)
        return (x[:, 0] + x[:, 1] > 1).astype(int).reshape(-1, 1)  # returns a matrix of (N, 1), elements either 0 or 1

## Usage

Call the `plot` method, passing your data, and the classification function as a lambda:

    import decision_boundary
    decision_boundary.plot(data.X_all, data.Y_all, classification_function)

You'll get something like this:

<img src="https://raw.githubusercontent.com/nusco/decision-boundary/master/example.jpg" width="250">
