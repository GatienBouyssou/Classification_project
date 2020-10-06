import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mp


if __name__ == '__main__':
    # get data
    data = np.loadtxt("data.txt", delimiter=", ")
    X, Y, Z = data[:, 1], data[:, 2], data[:, 3] # extract x, y and size

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    print(Z)
    ax.scatter(X, Y, Z, c='r', marker='o')
    ax.set_xlabel('x axis')
    ax.set_ylabel('y axis')
    ax.set_zlabel('z axis')

    plt.show()


