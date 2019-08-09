#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""====================================
# @Time    : 2019/8/9 14:01
# @Author  : Jing
# @FileName: 120. Triangle.py
# @IDE: PyCharm
======================================="""
# https://leetcode.com/problems/triangle/
# Solution 1: O(n*n/2) space, top-down
# Solution 2: Modify Solution, top-down



class Solution:
    def minimumTotal1(self, triangle):
        res = [[0 for i in row] for row in triangle]
        res[0][0] = triangle[0][0]
        n = len(triangle)
        for i in range(1, n):
            for j in range(len(triangle[i])):
                if j == 0:
                    res[i][j] += res[i-1][j]+triangle[i][j]
                elif j == len(triangle[i])-1:
                    res[i][j] += res[i-1][j-1]+triangle[i][j]
                else:
                    res[i][j] += min(res[i-1][j-1], res[i-1][j])+triangle[i][j]
        return min(res[-1])

    def minimumTotal2(self, triangle):
        if not triangle:
            return
        n = len(triangle)
        for i in range(1, n):
            for j in range(len(triangle[i])):
                if j == 0:
                    triangle[i][j] += triangle[i - 1][j]
                elif j == len(triangle[i]) - 1:
                    triangle[i][j] += triangle[i - 1][j - 1]
                else:
                    triangle[i][j] += min(triangle[i - 1][j - 1], triangle[i - 1][j])
        return min(triangle[-1])

    def minimumTotal3(self, triangle):
        n = len(triangle)
        for i in range(n - 2, -1, -1):
            for j in range(len(triangle[i])):
                triangle[i][j] += min(triangle[i + 1][j], triangle[i + 1][j + 1])
        return triangle[0][0]

    def minimumTotal4(self, triangle):
        res = triangle[-1]
        n = len(triangle)
        for i in range(n - 2, -1, -1):
            for j in range(len(triangle[i])):
                res[j] = min(res[j], res[j + 1]) + triangle[i][j]
        return res[0]


if __name__ == '__main__':
    a = [
        [2],
        [3, 4],
        [6, 5, 7],
        [4, 1, 8, 3]]
    s = Solution()
    print(s.minimumTotal1(a))               # Output is 11