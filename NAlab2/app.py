from Gauss import Gauss
from SquareRoots import SquareRoots
from Running import Running
from LQ import LQ
from datetime import datetime
import numpy as np


def print_m(A):
    string = ""
    for i in range(0, len(A)):
        for number in A[i]:
            string += '{:8}'.format(round(number, 3))
        string += "\n"
    print(string, "\n")


def print_a(A):
    string = ""
    for number in A:
        string += '{:8}'.format(round(number, 3))
    print(string, "\n")

def string_equation(matrix, b):
    string = ""
    letters = ["q", "w", "r", "t", "y", "u", "x", "z", "c"]
    for i in range(len(matrix[0])):
        for j in range(len(matrix[0])):
            string += letters[j] + "*(" + str(matrix[i][j]) + ")) +"
        string = string[0:len(string)-1]
        string += "= " + str(b[i]) + ",\n"
    string = string[0:len(string) - 1]
    return string


def print_arr(arr):
    string = ""
    for i in arr:
        string += str(round(i, 3)) + "\t"
    print(string)


matrix_small = [[1, 2, 3],
                [5, 6, 7],
                [9, 7, 3]]

b_small = [4, 8, 3]

matrix1 = [[10, -28, -8, 96, -50, 66, -8, 28, 56],
           [3, 87, 95, -70, 2, -61, 17, -22, 95],
           [63, -59, -84, 81, 46, 90, 71, -90, 35],
           [42, -72, -43, 65, 52, 47, 88, 66, -99],
           [-36, -100, 10, -30, 51, -82, 1, -28, -22],
           [9, 24, 73, 29, 46, -50, -98, 27, -73],
           [50, 57, 43, 15, 97, -62, -13, 38, 3],
           [74, 13, 41, -78, -30, 0, 67, 26, 17],
           [65, -48, 42, 70, 67, -73, 83, -80, -43]]

b1 = [-42, 46, 70, -46, 36, -42, 36, 6, 45]

matrix2 = [[166, 125, 77, 65, 150, 90, 111, 1, 65, -4],
           [125, 228, -12, -83, 199, 8, 25, -17, 43, -27],
           [77, -12, 210, 124, 80, 78, 102, -86, 18, 65],
           [65, -83, 124, 232, 11, 36, 97, -23, 60, 74],
           [150, 199, 80, 11, 244, 52, 70, -51, 63, 6],
           [90, 8, 78, 36, 52, 227, 129, -36, 44, 27],
           [111, 25, 102, 97, 70, 129, 234, -105, 1, 107],
           [1, -17, -86, -23, -51, -36, -105, 221, 14, -199],
           [65, 43, 18, 60, 63, 44, 1, 14, 116, -13],
           [-4, -27, 65, 74, 6, 27, 107, -199, -13, 248]]

b2 = [-82, -232, 185, 212, 189, 90, -58, -153, 183, -104]

matrix3 = [[-364, -277, 0, 0, 0, 0, 0, 0, 0, 0],
           [128, 880, -18, 0, 0, 0, 0, 0, 0, 0],
           [0, 12, 279, 41, 0, 0, 0, 0, 0, 0],
           [0, 0, 19, 88, 2, 0, 0, 0, 0, 0],
           [0, 0, 0, -278, 988, -389, 0, 0, 0, 0],
           [0, 0, 0, 0, -341, -781, -75, 0, 0, 0],
           [0, 0, 0, 0, 0, -14, -103, 27, 0, 0],
           [0, 0, 0, 0, 0, 0, 69, 256, 110, 0],
           [0, 0, 0, 0, 0, 0, 0, -291, 946, -341],
           [0, 0, 0, 0, 0, 0, 0, 0, -319, 393]]

b3 = [51, 61, 723, -30, -213, 343, 483, 40, -305, -700]
print("завдання 1-----------------------------------------------------------------------------------------------------")
print("Gauss")
gauss = Gauss(matrix1)

start = datetime.now()
print_a(Gauss.solve(gauss, b1))
end = datetime.now()

gauss = Gauss(matrix_small)
print(end-start)
print("LQ")

lq = LQ(matrix1)

start = datetime.now()
print_a(lq.solve(b1))

end = datetime.now()

print(end-start)

print(np.linalg.solve(np.asmatrix(matrix1), np.asarray(b1)))

print("завдання 2-----------------------------------------------------------------------------------------------------")
print("Square roots")
sq = SquareRoots(matrix2)

start = datetime.now()
print_a(sq.solve(b2))
end = datetime.now()

print(end-start)
print("Gauss")

gauss2 = Gauss(matrix2)
start = datetime.now()
print_a(gauss2.solve(b2))
end = datetime.now()
print(np.linalg.solve(np.asmatrix(matrix2), np.asarray(b2)))

print(end-start)

print("завдання 3-----------------------------------------------------------------------------------------------------")
print("Gauss")

gauss3 = Gauss(matrix3)

start = datetime.now()
print_a(gauss3.solve(b3))
end = datetime.now()

print(end-start)
print("Running")

running = Running(matrix3)

start = datetime.now()
print_a(running.solve(b3))
end = datetime.now()


print(np.linalg.solve(np.asmatrix(matrix3), np.asarray(b3)))

print(end-start)


