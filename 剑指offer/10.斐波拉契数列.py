# -*- coding: utf-8 -*-
# @Author  : Jing
# @FileName: 10.斐波拉契数列.py
# @IDE: PyCharm
# Solution 1: Recursion
# Solution 2: DP

def fibonacci1(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci1(n-1)+fibonacci1(n-2)


def fibonacci2(n):
    a, b = 0, 1
    if n < 2:
        return n
    for i in range(2, n+1):
        a, b = b, a+b
    return b


def fibonacci3(n):
    dp = [0 for _ in range(3)]
    dp[1] = 1
    for i in range(2, n+1):
        dp[i % 3] = dp[(i-1) % 3]+dp[(i-2) % 3]
    return dp[n % 3]


if __name__ == '__main__':
    n = 10
    print(fibonacci3(n))            # Output is 55.
