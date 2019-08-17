#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""====================================
# @Time    : 2019/8/16 23:06
# @Author  : Jing
# @FileName: 62. Unique Paths.py
# @IDE: PyCharm
======================================="""
# https://leetcode.com/problems/unique-paths/
# Solution 1: O(MN)Time O(MN)Space
# Solution 2: O(MN)Time O(N)Space


class Solution:
    def uniquePaths1(self, m, n):
        dp = [[1]*n for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j]+dp[i][j-1]
        return dp[-1][-1]

    def uniquePaths2(self, m, n):
        dp = [[1] * n for _ in range(2)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i%2][j] = dp[(i-1)%2][j] + dp[i%2][j - 1]
        return dp[(m-1)%2][-1]


if __name__ == '__main__':
    m, n = 3, 2
    s = Solution()
    print(s.uniquePaths2(m, n))              # Output is 3.