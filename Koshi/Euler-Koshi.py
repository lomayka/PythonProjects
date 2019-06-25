import math
import matplotlib.pyplot as plt


def Euler_Cauchy(x_start, y_start, x_end, n, f):
    x0 = x_start
    y0 = y_start
    Xs = [x_start]
    Ys = [y_start]
    h = (x_end - x_start) / n
    for i in range(1, n + 1):
        dy = f(x0, y0)
        ye = y0 + h * dy
        yec = ye
        for k in range(1, 5):
            yec = y0 + h / 2 * (dy + f(x0 + h, yec))
        x0 += h
        y0 = yec
        Xs.append(x0)
        Ys.append(y0)
    return Xs, Ys


def Runge_Kutta(x_start, y_start, x_end, n, f):
    xi = x_start
    yi = y_start
    Xs = [x_start]
    Ys = [y_start]
    h = (x_end - x_start) / n
    for i in range(1, n + 1):
        k1 = f(xi, yi)
        k2 = f(xi + h/2, yi + h / 2 * k1)
        k3 = f(xi + h/2, yi + h / 2 * k2)
        k4 = f(xi + h, yi + h * k3)
        dy = h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        xi += h
        Xs.append(xi)
        yi += dy
        Ys.append(yi)
    return Xs, Ys



def function(x, y):
    return y * x + x ** 3


x = 16
y = 7
x_end = 16.5
n = 17

X, Y = Euler_Cauchy(x, y, x_end, n, function)

print("Euler-Cauchy")
for xi, yi in zip(X, Y):
    print(xi, "~~~", yi)

plt.subplot(211)
plt.plot(X, Y)

Xs, Ys = Runge_Kutta(x, y, x_end, n, function)

print("Runge-Kutta")
for xi, yi in zip(Xs, Ys):
    print(xi, "---", yi)

plt.subplot(212)
plt.plot(Xs, Ys)
plt.show()