import copy

import numpy as np


class SquareRoots:
    a = np.zeros((10, 10))
    u = np.zeros((10, 10))
    ut = np.zeros((10, 10))

    def __init__(self, array):
        self.set_u(array)
        self.a = array
        self.ut = self.get_ut()

    def solve(self, arguments):
        _ut = copy.deepcopy(self.ut)
        _u = copy.deepcopy(self.u)
        b = copy.deepcopy(arguments)
        y = [0] * len(_u)
        x = [0] * len(_u)
        for i in range(len(_u)):
            m = 0
            for k in range(i):
                m = m + _ut[i][k] * y[k]
            y[i] = (b[i] - m) / _ut[i][i]
        for i in range(len(_u) - 1, -1, -1):
            m = 0
            for k in range(i + 1, len(_u)):
                m = m + _u[i][k] * x[k]
            x[i] = (y[i] - m) / _u[i][i]
        return x

    def set_u(self, array):
        u = np.zeros((10, 10))
        a = copy.deepcopy(array)
        for i in range(len(a)):
            for j in range(len(a)):
                s = 0
                if i == j:
                    for k in range(i):
                        s += u[k][i] ** 2
                    u[i][i] = np.sqrt(a[i][i] - s)
                if i < j:
                    for k in range(i):
                        s += u[k][i] * u[k][j]

                    u[i][j] = (a[i][j] - s) / u[i][i]
                if i > j:
                    u[i][j] = 0
        self.u = copy.deepcopy(u)

    def get_ut(self):
        return np.array(self.u).transpose()

    @staticmethod
    def print_m(A):
        string = ""
        for i in range(0, len(A)):
            for number in A[i]:
                string += '{:8}'.format(round(number, 3))
            string += "\n"
        print(string, "\n")

    @staticmethod
    def print_arr(arr):
        string = ""
        for i in arr:
            string += str(round(i, 3)) + "\t"
        print(string)

    def get_determinant(self):
        det = 1
        for i in range(len(self.u)):
            det = det * self.u[i][i]
        det = pow(det, 2)
        return det

    def get_reverse(self):
        reverse = []
        for i in range(len(self.u)):
            reverse.append([0] * len(self.u))
        for i in range(len(self.u) - 1, -1, -1):
            for j in range(len(self.u) - 1, -1, -1):
                if i < j:
                    m = 0
                    for k in range(i + 1, len(self.u)):
                        m = m + reverse[k][j] * self.u[i][k]
                    reverse[i][j] = - m
                elif i == j:
                    m = 0
                    for k in range(j + 1, len(self.u)):
                        m = m + reverse[i][k] * self.ut[k][j]
                    reverse[i][j] = (1 - m) / self.ut[j][j]
                elif i > j:
                    m = 0
                    for k in range(j + 1, len(self.u)):
                        m = m + reverse[i][k] * self.ut[k][j]
                    reverse[i][j] = -m / self.ut[j][j]
        return reverse
