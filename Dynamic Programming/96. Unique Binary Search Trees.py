#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""====================================
# @Time    : 2019/8/9 11:50
# @Author  : Jing
# @FileName: 96. Unique Binary Search Trees.py
# @IDE: PyCharm
======================================="""
# https://leetcode.com/problems/unique-binary-search-trees/
# Solution 1: f(n) = f(0)*f(n-1)+...+f(n-1)*f(0)
# eg. f(4)=f(0)*f(3)+f(1)*f(2)+f(2)*f(1)+f(3)*f(0)
# Solution 2: Catalan Number  (2n)!/((n+1)!*n!
import math


class Solution:
    def numTrees1(self, n: int) -> int:
        res = [0 for _ in range(n+1)]
        res[0] = 1
        for i in range(1, n+1):
            for j in range(i):
                res[i] += res[j]*res[i-1-j]
        return res[n]

    def numTrees2(self, n):
        return int(math.factorial(2*n)/(math.factorial(n)*math.factorial(n+1)))


if __name__ == '__main__':
    s = Solution()
    n = 3
    print(s.numTrees1(n))               # Output is 5
