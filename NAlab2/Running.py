import copy


class Running:
    arr = [[]]

    def __init__(self, array):
        self.arr = array

    def solve(self, arguments):
        b = copy.deepcopy(arguments)
        array = copy.deepcopy(self.arr)
        length = len(array[0])

        l = [0] * length
        delta = [0] * length
        x = [0] * length

        for i in range(length):
            r = b[i]

            if i == 0:
                u = 0
            else:
                u = array[i][i - 1]
            if i == length - 1:
                d = 0
            else:
                d = array[i][i + 1]
            c = array[i][i]
            delta[i] = -d / (c + u * delta[i - 1])
            l[i] = (r - u * l[i - 1]) / (c + u * delta[i - 1])

        x[length-1] = l[length-1]

        for i in range(length - 2, -1, -1):
            x[i] = delta[i] * x[i + 1] + l[i]
        return x

    @staticmethod
    def print_m(self, A):
        string = ""
        for i in range(0, len(A)):
            for number in A[i]:
                string += '{:8}'.format(round(number, 3))
            string += "\n"
        print(string, "\n")