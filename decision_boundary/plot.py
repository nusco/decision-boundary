# The boundary-plotting code has been adapted from the scikit-learn
# documentation, that comes with a BSD license:
#
# Copyright (c) <year>, <copyright holder>
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice, this
#    list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
# ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
# The views and conclusions contained in the software and documentation are those
# of the authors and should not be interpreted as representing official policies,
# either expressed or implied, of the <project name> project.

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import seaborn as sns


# Generate a mesh over one-dimensional data x
def mesh(x, resolution, padding_percent):
    range = x.max() - x.min()
    padding_absolute = range * padding_percent * 0.01
    interval = (range + 2 * range * padding_absolute) / resolution
    return np.arange(x.min() - padding_absolute, x.max() + padding_absolute, interval)


def plot_boundary(x, y, classification_function, resolution=1000, padding_percent=5):
    # Generate a grid of points over the data
    x_mesh = mesh(x, resolution, padding_percent)
    y_mesh = mesh(y, resolution, padding_percent)
    grid_x, grid_y = np.meshgrid(x_mesh, y_mesh)
    grid = np.c_[grid_x.ravel(), grid_y.ravel()]
    # Classify points in the grid
    classifications = classification_function(grid).reshape(grid_x.shape)
    # Trace the decision boundary
    GREEN_AND_BLUE = ListedColormap(['#AAFFAA', '#AAAAFF'])
    plt.contourf(grid_x, grid_y, classifications, cmap=GREEN_AND_BLUE)


def plot_data_by_label(features, labels, label_selector, symbol):
    points = features[(labels == label_selector).flatten()]
    plt.plot(points[:, 0], points[:, 1], symbol)


def plot_data(data, labels):
    plot_data_by_label(data, labels, 0, 'g*')
    plot_data_by_label(data, labels, 1, 'bp')


def show():
    plt.show()
