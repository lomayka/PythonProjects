import copy


class Gauss:
    arr = [[]]

    def __init__(self, array):
        self.arr = array

    @staticmethod
    def print_m(A):
        string = ""
        for i in range(0, len(A)):
            for number in A[i]:
                string += '{:10}'.format(round(number, 3))
            string += "\n"
        print(string, "\n")

    def solve(self, arguments):
        array = copy.deepcopy(self.arr)
        length = len(self.arr)
        b = copy.deepcopy(arguments)
        for k in range(length):
            first = array[k][k]
            for j in range(k, length):
                array[k][j] /= first
            b[k] /= first
            for i in range(k+1, length):
                col = array[i][k]
                for j in range(k, length):
                    array[i][j] -= array[k][j]*col
                b[i] -= b[k] * col
                #self.print_m(array)

        for i in reversed(range(0, length)):
            for k in reversed(range(0, i)):
                b[k] -= array[k][i] * b[i]
                array[k][i] *= 0

        x = [0] * length
        for t in range(length-1, -1, -1):
            s = 0
            for j in range(t+1, length):
                s += array[t][j]*b[j]
            x[t] = b[t] - s

        return x

    def determinant(self):
        array = self.arr
        length = len(self.arr[0])
        res = []

        for i in range(0, length):
            first = array[i][i]
            res.append(first)
            for k in range(i, length):
                array[i][k] /= first

            for j in range(i + 1, length):
                for p in range(0, length):
                    array[j][p] -= array[i][p] * array[j][i]

        det = 1
        for i in res:
            det *= i
        return det

    def inverse(self):
        array = self.arr
        length = len(self.arr[0])
        inverted = []
        for i in range(0, length):
            inverted.append([])
            for j in range(0, length):
                if i is j:
                    inverted[i].append(1)
                else:
                    inverted[i].append(0)

        for i in range(0, length):
            first = array[i][i]
            for k in range(i, length):
                array[i][k] /= first
            for k in range(0, length):
                inverted[i][k] /= first

            for j in range(i + 1, length):
                for p in range(0, length):
                    array[j][p] -= array[i][p] * array[j][i]
                    inverted[j][p] -= inverted[i][p] * inverted[j][i]

        for i in reversed(range(0, length)):
            for k in reversed(range(0, i)):
                for j in range(0, length):
                    inverted[k][j] -= inverted[i][j] * self.arr[k][i]
                self.arr[k][i] *= 0
        return inverted

    def print_arr(self, arr):
        string = ""
        for i in arr:
            string += str(round(i, 3)) + "\t"
        print(string)
