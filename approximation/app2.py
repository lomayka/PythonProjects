from builtins import range, len, float, open

import matplotlib.pyplot as plt

import numpy as np


def coef(x, y):
    n = len(x)
    a = []
    for i in range(n):
        a.append(y[i])

    table = []
    table.append(a)

    for j in range(1, n):
        table.append([])
        for i in range(1, n - j + 1):
            table[j].append((table[j-1][i] - table[j-1][i - 1])/(x[i + j - 1] - x[i - 1]))

    return table


def Eval(table, x, r):
    n = len(table[0]) - 1
    sum = table[0][n]
    for i in range(1, n):
        temp = table[i][n - i]
        for j in range(0, i):
            temp *= r - x[n - j]
        sum += temp
    return sum

strings = open("x_yurchik", "r").read().split("\n")
x = [float(x) for x in strings]

strings = open("y_yurchik", "r").read().split("\n")
y = [float(y) for y in strings]
strings = open("points2_yurchik").read().split("\n")
points = [float(points) for points in strings]

table = coef(x, y)
for list in table:
    print(len(list), list)
values = []
for point in points:
    values.append(Eval(table, x, point))

for value in values:
    print("%.2f" % value)

plt.subplot(211)
plt.plot(x, y)
plt.subplot(212)
#plt.axis([x[0], x[-1], -100, y[-1]])

plt.plot(points, values)
plt.show()
