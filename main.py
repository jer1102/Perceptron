import numpy as np
from numpy import random
import matplotlib.pyplot as plt
import pandas as pd

a = .1
b = .4
c = 6
exp = 1.3
x1 = np.linspace(0, 20)
y1 = a * x1 + b * x1 ** exp + c
# y1 = 5*np.sin(2*x1) + 10

x = np.array(random.randint(20, size=40))
y = np.array(random.randint(20, size=40))
classes = np.array(y >= a * x + b * x ** exp + c)
# classes = np.array(y > 5*np.sin(2*x) + 10)
classes = classes * 1


def color_picker(col):
    if classes[col]:
        return 'blue'
    else:
        return 'red'


color = np.array(
    ['black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black',
     'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black',
     'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black',
     'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black'])

for i in range(40):
    color[i] = color_picker(i)

data = {'X': x, 'Y': y, 'Class': classes, 'Colors': color}
dataset = pd.DataFrame(data)
plt.index = 'Thing'
plt.scatter(x, y, c=color)
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('Graph 7: less layover')
plt.plot(x1, y1)
plt.xlim(0, 20)
plt.ylim(0, 20)
plt.savefig('graph7.png')
plt.show()
dataset.to_csv('graph7csv')

