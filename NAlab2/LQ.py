import copy

import numpy as np


class LQ:
    arr = [[]]

    def __init__(self, array):
        self.arr = array

    def solve(self, arguments):
        length = len(self.arr)

        A = copy.deepcopy(self.arr)
        Q = []
        y = [0] * length
        for i in range(length-1):
            sum = 0
            for k in range(i, length):
                sum += np.power(A[i][k], 2)
            beta = np.sign(-A[i][i]) * np.sqrt(sum)
            mu = 1/np.sqrt(2 * np.power(beta, 2) - 2 * beta * A[i][i])
            w = []
            for j in range(0, length):
                if j < i:
                    w.append(0)
                elif j == i:
                    w.append(((A[i][i]) - beta) * mu)
                else:
                    w.append(mu * A[i][j])

            H = []
            for j in range(length):
                H.append([])
                for k in range(length):
                    if j == k:
                        H[j].append(1 - 2 * w[j] * w[j])
                    else:
                        H[j].append(-2 * w[j] * w[k])
            if i == 0:
                Q = copy.deepcopy(H)
            else:
                Q = np.matrix.dot(np.asmatrix(Q), np.asmatrix(H)).tolist()
            A = np.matrix.dot(np.asmatrix(A), np.asmatrix(H)).tolist()
            self.print_m(A)

        y = []

        for i in range(0, length):
            sum = 0
            for k in range(i):
                sum += A[i][k] * y[k]
            y.append((arguments[i] - sum)/A[i][i])

        x = np.dot(np.asmatrix(Q), np.asarray(y)).tolist()[0]
        return x



    @staticmethod
    def print_m(A):
        string = ""
        for i in range(0, len(A)):
            for number in A[i]:
                string += '{:10}'.format(round(number, 3))
            string += "\n"
        print(string, "\n")