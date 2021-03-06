#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Fibonacci numbers module


def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while b < n:
        print b,
        a, b = b, a + b


def fib2(n):  # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a + b
    return result

# 1. one methond
# >>> import fibo
# >>> fibo.fib(1000)
# 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987
# >>> fibo.fib2(100)
# [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# >>> fibo.__name__
# 'fibo'

# 2. another method
# >>> from fibo import fib, fib2
# >>> fib(500)
# 1 1 2 3 5 8 13 21 34 55 89 144 233 377