import math


def coin_toss_probability(k1, k2, n, p):

    res = 0
    for i in range(k1, k2+1):
        res += math.factorial(n)/(math.factorial(i)*math.factorial(n-i)) * (p ** i) * ((1-p) ** (n-i))
    return res


print(coin_toss_probability(10, 60, 100, 0.2))
