from builtins import range, len, format
import math


class SecondNewton:

    def __init__(self, originalFunc, lastX, n, h):
        self.originalFunc = originalFunc
        self.x = []
        self.n = n
        self.h = h
        self.subTable = []
        self.lastX = lastX

    def fillPoints(self):
        self.subTable.append([])
        start = self.lastX - self.h * self.n * 2
        for i in range(0, self.n * 2):
            self.x.append((i + 1) * self.h + start)
            self.subTable[0].append(self.originalFunc(self.x[i]))


    def printSubTable(self):
        for row in self.subTable:
            separator = ' '
            print(len(row), " - ", " ".join(format(x, "8.5f") for x in row))

    def fillSubTable(self):

        for i in range(1, self.n * 2):
            flag = 0
            self.subTable.append([])
            for j in range(0, self.n * 2 - i):
                val = self.subTable[i - 1][j + 1] - self.subTable[i - 1][j]
                self.subTable[i].append(val)

                if abs(val) > 5 * math.pow(10, -10):
                    flag = 1
            if flag is 0:
                print(i)
                self.subTable.pop()
                break

    def getApproximatedFunc(self):

        def approximated(x):

            n = self.n * 2

            result = self.subTable[0][n-1]
            q = (x - self.lastX)/self.h

            for i in range(n - 1, 0, -1):
                m = n - i

                mul = 1
                for k in range(m):
                    mul *= q - k

                result += mul / math.factorial(m) * self.subTable[m-1][i]

            return result

        return approximated
