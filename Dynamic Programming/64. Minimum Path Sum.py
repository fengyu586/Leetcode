#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""====================================
# @Time    : 2019/8/10 16:58
# @Author  : Jing
# @FileName: 64. Minimum Path Sum.py
# @IDE: PyCharm
======================================="""
# https://leetcode.com/problems/minimum-path-sum/
# Solution 1: O(MN) Time and O(MN) Space
# Solution 2: O(MN) Time and O(M) Space
# Solution 3: a litter faster than the above solution


class Solution:
    def minPathSum1(self, grid):
        n = len(grid)
        m = len(grid[0])
        dp = [[0 for _ in range(m)] for i in range(n)]
        dp[0][0] = grid[0][0]
        for i in range(1, m):
            dp[0][i] = dp[0][i-1]+grid[0][i]
        for i in range(1, n):
            dp[i][0] = dp[i-1][0]+grid[i][0]
        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1])+grid[i][j]
        return dp[-1][-1]

    def minPathSum2(self, grid):
        n = len(grid)
        m = len(grid[0])
        dp = [[0 for _ in range(m)] for i in range(2)]
        for i in range(n):
            for j in range(m):
                if i == 0 and j == 0:
                    dp[i][j] = grid[i][j]
                elif i == 0 and j != 0:
                    dp[i][j] = dp[i][j - 1] + grid[i][j]
                elif i != 0 and j == 0:
                    dp[i % 2][j] = dp[(i + 1) % 2][j] + grid[i][j]
                else:
                    dp[i % 2][j] = min(dp[(i + 1) % 2][j], dp[i % 2][j - 1]) + grid[i][j]
        return dp[(n+1)%2][-1]

    def minPathSum3(self, grid):
        n = len(grid)
        m = len(grid[0])
        dp = [[0 for _ in range(m)] for i in range(2)]
        for i in range(n):
            for j in range(m):
                if i == 0:
                    if j == 0:
                        dp[i][j] = grid[i][j]
                    else:
                        dp[i][j] = dp[i][j - 1] + grid[i][j]
                else:
                    if j == 0:
                        dp[i % 2][j] = dp[(i + 1) % 2][j] + grid[i][j]
                    else:
                        dp[i % 2][j] = min(dp[(i + 1) % 2][j], dp[i % 2][j - 1]) + grid[i][j]
        return dp[(n + 1) % 2][-1]


if __name__ == '__main__':
    a = [[1,3,1],
        [1,5,1],
        [4,2,1]]
    s = Solution()
    print(s.minPathSum2(a))             # Output is 7
