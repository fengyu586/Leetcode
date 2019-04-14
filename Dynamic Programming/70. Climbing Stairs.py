#!/usr/bin/python3.6
# -*- coding:utf-8 -*-
# https://leetcode.com/problems/climbing-stairs/
# 1.最后一步
# 2.子问题
# 3.初始条件及边界条件
# 4. 状态转移方程
# 5. 顺序问题


class Solution:
    def climbStairs(self, n: int) -> int:
        res = [1, 1]
        for i in range(1, n):
            res += [res[-1]+res[-2]]
        return res[-1]


