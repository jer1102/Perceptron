import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from numpy import random

l_rate = 128
w0 = random.randint(-10, 10)
w1 = random.randint(-10, 10)
w2 = random.randint(-10, 10)
dataset = pd.read_csv('/home/jered/PycharmProjects/Perceptron/Graph 1 Data/graph1csv')
X = np.array(dataset.X)
Y = np.array(dataset.Y)
classes = np.array(dataset.Class)
color = np.array(dataset.Colors)


def weight_checker(x, y):
    global w0, w1, w2
    if w0 * 1 + w1 * x + w2 * y >= 0:
        return 1
    else:
        return 0


def weight_updater(x, y, cx, hx):
    global w0, w1, w2, l_rate
    w0 = w0 + l_rate * (cx - hx) * 1
    w1 = w1 + l_rate * (cx - hx) * x
    w2 = w2 + l_rate * (cx - hx) * y


epoch = 0
i = 0
num = 0
checker = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
while True:
    plt.clf()
    print(i)
    classof = weight_checker(X[i], Y[i])
    checker[i] = classes[i] - classof
    w0 = w0 + l_rate * (classes[i] - classof) * 1
    classof = weight_checker(X[i], Y[i])
    w1 = w1 + l_rate * (classes[i] - classof) * X[i]
    classof = weight_checker(X[i], Y[i])
    w2 = w2 + l_rate * (classes[i] - classof) * Y[i]
    print("edited: ", w0, w1, w2)
    x1 = np.linspace(0, 20)
    y1 = (w0 + w1 * x1)/-w2*1
    plt.scatter(X, Y, color=color)
    plt.plot(x1, y1, color='green')
    plt.xlabel('X axis')
    plt.ylabel('Y axis')
    plt.xlim(0, 20)
    plt.ylim(-20, 20)
    if checker[i] != 0:
        plt.title('Graph iteration: ' + str(40*epoch + i))
        plt.savefig("Graph8-" + str(num) + ".png")
        plt.show()
        num += 1

    if i == 39:
        for g in range(39):
            if checker[g] != 0:
                epoch += 1
                i = 0
                print('break!')
                break
        if i != 0:
            break
    i += 1




