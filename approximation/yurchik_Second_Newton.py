import math
from builtins import float, open
from SecondNewton import SecondNewton
import matplotlib.pyplot as plt


def func(x):
    return x * math.sin(x) + x ** 2 * math.exp(x) + math.log(x ** 3, 2)


strings = open("points1_yurchik", "r").read().split("\n")
points = [float(point) for point in strings]

strings = open("points1_yurchik", "r").read().split("\n")
strings.pop()
ys = [float(point) for point in strings]



newton = SecondNewton(func, 7.2, 25, 0.08)

newton.fillPoints()
newton.fillSubTable()
approx = newton.getApproximatedFunc()

approx_vals = []
func_vals = []
errors = []
newton.printSubTable()
for point in points:
    a = approx(point)
    approx_vals.append(a)
    b = func(point)
    func_vals.append(b)
    print(a, " ~~~ ", b)
    print(a - b)
    errors.append(a - b)

plt.subplot(211)
plt.plot(approx_vals, points)
plt.plot(func_vals, points)

plt.subplot(212)
plt.plot(points, errors)
plt.show()
