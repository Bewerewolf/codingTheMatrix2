import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy
from mpl_toolkits.mplot3d.axes3d import Axes3D
import numpy as np
import sympy

def test_plot():
    x = np.linspace(-5, 2, 100)
    y1 = x**3 + 5*x**2 + 20
    y2 = 3*x**2 + 10*x
    y3 = 6*x + 10

    fig, ax = plt.subplots()
    ax.plot(x, y1, color="blue", label="y(x)")
    ax.plot(x, y2, color="red", label="y'(x)")
    ax.plot(x, y3, color="green", label="y''(x)")
    ax.set_xlabel("x")
    ax.set_xlabel("y")
    ax.legend()
    plt.show()

def main():
    test_plot()



if __name__ == '__main__':
    main()