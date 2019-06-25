import math
import matplotlib.pyplot as plt


def Heun_func(y, h, x, f):
    return y + h/2 * (f(x, y) + f(x + h, y + h * f(x, y)))


def Heun(x0, y0, b, f, n):
    h = (b - x0)/n
    y = y0
    Xs = []
    Ys = []
    for i in range (0, n + 1):
        y = Heun_func(y, h, x0 + i * h, f)
        Xs.append(x0 + i * h)
        Ys.append(y)
    return Xs, Ys


def Kutta_Merson(x0, y0, b, f, n, epsilon):
    h = (b - x0)/n
    y = y0
    i = 0
    x = x0
    Xs = []
    Ys = []
    while x < b:
        x_temp = x + h
        k1 = f(x_temp, y)
        k2 = f(x_temp + h/3, y + h/3 * k1)
        k3 = f(x_temp + h/3, y + h/6 * k1 + 3*h/8 * k2)
        k4 = f(x_temp + h/2, y + h/8 * k1 + 3*h/8 * k2)
        k5 = f(x_temp + h, y + h/2 * k1 - 3 * h/2 * k3 + 2 *h * k4)
        y_tilda = y + h/2 * (k1 - 3 * k3 + 2 * h * k4)
        y_temp = y + h/6 * (k1 + 4 * k4 + k5)
        if 0.2 * abs(y_temp - y_tilda) < epsilon:
            x = x_temp
            y = y_temp
            Xs.append(x)
            Ys.append(y)
            i += 1
#            print(i, x, y)
        else:
            h = h/2
    return Xs, Ys

# def Kutta_Merson(x0, y0, b, f, n, epsilon):
#     h = (b - x0)/n
#     y = y0
#     i = 0
#     x = x0
#     while i < n:
#         x_temp = x + h
#         k1 = f(x_temp, y)
#         k2 = f(x_temp + h/3, y + h/3 * k1)
#         k3 = f(x_temp + h/3, y + h/6 * k1 + 3*h/8 * k2)
#         k4 = f(x_temp + h/2, y + h/8 * k1 + 3*h/8 * k2)
#         k5 = f(x_temp + h, y + h/2 * k1 - 3 * h/2 * k3 + 2 *h * k4)
#         y_tilda = y + h/2 * (k1 - 3 * k3 + 2 * h * k4)
#         y_temp = y + h/6 * (k1 + 4 * k4 + k5)
#         print(0.2 * abs(y_temp - y_tilda))
#         if 0.2 * abs(y_temp - y_tilda) < epsilon:
#             x = x_temp
#             y = y_temp
#             i += 1
#             print(i, x, y)
#         else:
#             h = h/2
#     print(x, y)


def function(x, y):
    return x * math.log(y) + y


x0 = 9
y0 = 1
b = 11
n = 21
epsilon = 10 ** -5

HeunX, HeunY = Heun(x0, y0, b, function, n)
MersonX, MersonY = Kutta_Merson(x0, y0, b, function, n, epsilon)

plt.subplot(211)
plt.plot(HeunX, HeunY)
plt.subplot(212)
plt.plot(MersonX, MersonY)
plt.show()
