#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""====================================
# @Time    : 2019/8/16 15:42
# @Author  : Jing
# @FileName: 279. Perfect Squares.py
# @IDE: PyCharm
======================================="""
# https://leetcode.com/problems/perfect-squares/
# Solution 1: O(n^3/2)Time O(n)Space
# Solution 2: O(n)Time O(n)Space
# 满足四数平方和定理的数n（这里要满足由四个数构成，小于四个不行），
# 必定满足 n=4^a(8b + 7)
# Lagrange 四平方定理：
# 任何一个正整数都可以表示成不超过四个整数的平方之和。
# 我们首先将输入的n迅速缩小。然后我们再判断，
# 这个缩小后的数是否可以通过两个平方数的和或一个平方数组成，
# 不能的话我们返回3，能的话我们返回平方数的个数。

class Solution:
    def numSquares(self, n):
        dp = [float('inf')]*(n+1)
        dp[0] = 0.0
        for i in range(1, n+1):
            j = 1
            while j*j <= i:
                dp[i] = min(dp[i], dp[i-j*j]+1)
                j += 1
        return int(dp[n])

    def numSquares1(self, n):
        while n % 4 == 0:
            n = n / 4
        if (n % 8 == 7):
            return 4

        a = 0
        while a ** 2 <= n:
            b = int((n - a ** 2) ** 0.5)
            if a ** 2 + b ** 2 == n:
                return (not not a) + (not not b)
            a += 1
        return 3


if __name__ == '__main__':
    a = 12
    b = 13
    s = Solution()
    print(s.numSquares(5254))          # Output is 3

