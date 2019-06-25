from sympy import *
import numpy as np


def IP(f, H, n, a):
    i = 0
    x = 0
    sum = 0
    while i < n:
        if i == 0:
            x = a + H / 2
        else:
            x = x + H
        sum += f(x)
        i += 1
    return sum * H


def trapezoid_rectangle(f, a, b, e):
    H = b - a
    n = 1
    IT = H / 2 * (f(a) + f(b))
    while True:
        Ip = IP(f, H, n, a)
        It = 1 / 2 * (Ip + IT)
        Rt = 1 / 3 * (It - IT)
        if abs(Rt) > e:
            n = 2 * n
            H = H / 2
            IT = It
        else:
            return It + Rt


def folded_trapezoid(f, n, a, b):
    h = ( b - a ) / n
    sum = (f(a) + f(b)) / 2
    for i in range(1, n):
        sum += f(a + h * i)
    return sum * h


def num_from_error_folded(a, b, f, sigma, epsilon):
    mid = b - a
    return int(round(sqrt(mid ** 3 / 12 * f(sigma) / epsilon) + 0.5, 0))


def num_from_error_simpson(a, b, f, sigma, epsilon):
    mid = b - a
    return int(round((-mid ** 5 / 180 * f(sigma) / epsilon) ** (1/4) + 0.5, 0))



def simpson(f, n, a, b):
    h = (b - a) / n
    m = n * 2
    sum = f(a) + f(b)
    for i in range(1, n, 2):
        sum += 4 * f(a + i * h)
    for i in range(2, n - 1, 2):
        sum += 2 * f(a + i * h)
    return sum * h / 3


start = 3
end = 10
epsilon = 10 ** -9
sigma = 7
x = symbols("X")


y = log(x ** 2) / x + cos(x) + x ** 3
f = lambdify(x, y, 'numpy')
dy4th = y.diff(x, 4)
dy2th = y.diff(x, 2)
d4y = lambdify(x, dy4th, 'numpy')
d2y = lambdify(x, dy2th, 'numpy')
n = num_from_error_simpson(start, end, d4y, sigma, epsilon)
m = num_from_error_folded(start, end, d2y, sigma, epsilon)
print(n)
print(m)

print(folded_trapezoid(f, m, start, end))
print(simpson(f, n * 2, start, end))
print(trapezoid_rectangle(f, start, end, epsilon))



