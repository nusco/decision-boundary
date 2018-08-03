name = "decision_boundary"

from . import plot

def show(data, labels, classification_function, resolution=1000, padding_percent=5):
    plot.plot_boundary(data[:, 0], data[:, 1], classification_function, resolution, padding_percent)
    plot.plot_data(data, labels)
    plot.show()
