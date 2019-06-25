from builtins import range, len, float, open

import matplotlib.pyplot as plt

import numpy as np


def coef(x, y):
    n = len(x)
    a = []
    for i in range(n):
        a.append(y[i])

    for j in range(1, n):
        for i in range(n - 1, j - 1, -1):
            a[i] = float(a[i] - a[i - 1]) / float(x[i] - x[i - j])

    return np.array(a)


def Eval(a, x, r):
    n = len(a) - 1
    temp = a[n]
    for i in range(n - 1, -1, -1):
        temp = temp * (r - x[i]) + a[i]
    return temp


strings = open("x.txt", "r").read().split("\n")
x = [float(x) for x in strings]

strings = open("y.txt", "r").read().split("\n")
y = [float(y) for y in strings]
strings = open("points1.txt").read().split("\n")
points = [float(points) for points in strings]

table = coef(x, y)
print(table)
values = []
for point in points:
    values.append(Eval(table, x, point))

for value in values:
    print("%.2f" % value)

plt.subplot(211)
plt.plot(x, y)
plt.subplot(212)
plt.axis([x[0], x[-1], -100, y[-1]])

plt.plot(points, values)
plt.show()
