from numpy.polynomial.legendre import leggauss
from math import *

LIMITS = [[0, pi / 2], [0, pi / 2]]


def converts(func2, value):
    return lambda y: func2(value, y)


def variable_conversion(a, b, t):
    return (b + a) / 2 + (b - a) * t / 2


def function(parameter):
    return lambda x, y: (4 / pi) * (1 - \
		exp(-parameter * 2 * cos(x) / (1 - \
			(sin(x) ** 2) * (cos(y) ** 2)))) * cos(x) * sin(x)


def gauss(func, a, b, num_of_nodes):
    args, coeffs = leggauss(num_of_nodes)
    res = 0

    for i in range(num_of_nodes):
        res += (b - a) / 2 * coeffs[i] * \
            func(variable_conversion(a, b, args[i]))

    return res


def simpson(func, a, b, num_of_nodes):
    if (num_of_nodes < 3 or num_of_nodes & 1 == 0):
        raise ValueError
    h = (b - a) / (num_of_nodes - 1)
    x = a
    res = 0
    for i in range((num_of_nodes - 1) // 2):
        res += func(x) + 4 * func(x + h) + func(x + 2 * h)
        x += 2 * h
    return res * (h / 3)


def result(func, n, m, tao):
    return simpson(lambda x: gauss(converts(func, x), \
		LIMITS[1][0], LIMITS[1][1], m), LIMITS[0][0], LIMITS[0][1], n)


def main():
    N = int(input("\033[36m» Введите N: "))
    M = int(input("» Введите M: "))
    tao = float(input("» Введите τ: "))

    print("Результат: ", result(function(tao),N, M, tao))


if __name__ == "__main__":
    main()
