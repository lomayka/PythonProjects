from sympy import *
import numpy as np


def quadrate(f, n, a, b):
    h = (b - a) / n
    halfh = h / 2
    x = a
    sum = 0
    i = 0
    while i < n:
        sum += h * f(x - halfh)
        x += h
        i += 1
    return sum


def trapezoid(f, a, b, N):
    h = (b - a) / N
    xi = np.linspace(a, b, N + 1)
    fi = f(xi)
    s = 0.0
    for i in range(1, N):
        s = s + fi[i]
    s = (h / 2) * (fi[0] + fi[N]) + h * s
    return s


def romberg(f, a, b, eps):
    Q = []
    converged = False
    i = 0
    while not converged:
        local = []
        N = 2 ** i
        local.append(trapezoid(f, a, b, N))
        for k in range(0, i):
            n = k + 2
            local.append(1.0/(4 ** (n - 1) - 1) * (4 ** (n - 1) * local[k] - Q[i - 1][k]))
        Q.append(local)
        if i > 0:
            if (abs(Q[i][k + 1] - Q[i][k])) < eps:
                converged = True
            else:
                i += 1
        if i == 0:
            i += 1
    return Q[i][k+1], N, converged, log(N, 2)


def num_from_error(a, b, f, sigma, epsilon):
    mid = b - a
    return round(sqrt(mid ** 3 / 24 * f(sigma) / epsilon) + 0.5, 0)


x = symbols("X")

start = 13
end = 29
sigma = 13

y = (x ** (1 / 5) + (5 * exp(x)) ** (1 / 5)) / (1 + sinh(x)) ** (1 / 5)
f = lambdify(x, y, 'numpy')
dy2nd = y.diff(x, 2)
d2 = lambdify(x, dy2nd, 'numpy')
n = num_from_error(start, end, d2, sigma,10 ** -9)
print(n)

print(y)
print(quadrate(f, n, start, end))
print(romberg(f, start, end, 10 ** -9))
