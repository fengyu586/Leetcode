#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""====================================
# @Time    : 2019/8/7 0:08
# @Author  : Jing
# @FileName: 264. Ugly Number II.py
# @IDE: PyCharm
======================================="""
# https://leetcode.com/problems/ugly-number-ii/


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [1]*n
        nxt0, nxt1, nxt2 = 2, 3, 5
        id0, id1, id2 = 0, 0, 0
        for i in range(1, n):
            nxt = min(nxt0, nxt1, nxt2)
            dp[i] = nxt
            if nxt == nxt0:
                id0 += 1
                nxt0 = dp[id0]*2
            if nxt == nxt1:
                id1 += 1
                nxt1 = dp[id1]*3
            if nxt == nxt2:
                id2 += 1
                nxt2 = dp[id2]*5
        return dp[-1]


if __name__ == '__main__':
    a = 10
    s = Solution()
    print(s.nthUglyNumber(10))      # Output is 12