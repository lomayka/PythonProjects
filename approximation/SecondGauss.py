from builtins import range, len, format
import math


class SecondGauss:

    def __init__(self, originalFunc, middleX, n, h):
        self.originalFunc = originalFunc
        self.x = []
        self.n = n
        self.h = h
        self.subTable = []
        self.middleX = middleX

    def fillPoints(self):
        self.subTable.append([])
        start = self.middleX - self.n * self.h
        for i in range(0, self.n * 2):
            self.x.append(i * self.h + start)
            self.subTable[0].append(self.originalFunc(self.x[i]))

    def printSubTable(self):
        for row in self.subTable:
            separator = ' '
            print(len(row), " - ", " ".join(format(x, "8.5f") for x in row))

    def fillSubTable(self):

        for i in range(1, self.n * 2 + 1):
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

            q = (x - self.middleX) / self.h
            result = self.subTable[0][self.n]
            for i in range(1, len(self.subTable) // 2):
                m = 2 * i - 1

                mul0 = 1
                for k in range(1, m + 1):
                    mul0 *= q + i - k

                mul1 = 1
                for k in range(1, 2 * i + 1):
                    mul1 *= q + i - k + 1

                result += (mul0 / math.factorial(m)) * self.subTable[m][-i + self.n] + \
                          (mul1 / math.factorial(2 * i)) * self.subTable[2 * i][-i + self.n]

            return result

        return approximated
