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


if __name__ == '__main__':
    a = 12
    b = 13
    s = Solution()
    print(s.numSquares(b))          # Output is 3

