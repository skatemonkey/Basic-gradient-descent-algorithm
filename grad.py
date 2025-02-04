import numpy as np
import matplotlib.pyplot as plt


def y_function(x):
    return x ** 2


def y_function_derivative(x):
    return 2 * x


x = np.arange(-100, 100, 0.1)
y = y_function(x)

current_pos = (50, y_function(50))

learning_rate = 0.01

for i in range(100):
    new_x = current_pos[0] - learning_rate * y_function_derivative(current_pos[0])
    new_y = y_function(new_x)
    current_pos = (new_x, new_y)

    plt.plot(x, y)
    plt.scatter(current_pos[0], current_pos[1], color='red')
    plt.pause(0.1)
    plt.clf()


