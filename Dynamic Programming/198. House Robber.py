#!/usr/bin/python3.6
# -*- coding:utf-8 -*-
# https://leetcode.com/problems/house-robber/


class Solution:
    def rob1(self, nums):
        n = len(nums)
        if n == 0:
            return 0
        res = [0]*n
        for i in range(n):
            if i == 0:
                res[i] = nums[i]
            elif i == 1:
                res[i] = max(nums[0], nums[1])
            else:
                res[i] = max(res[i-2]+nums[i], res[i-1])
        return res[-1]

    def rob2(self, nums):
        n = len(nums)
        if n == 0:
            return 0
        if n < 3:
            return max(nums)
        res = [0] * n
        res[0], res[1] = nums[0], max(nums[0], nums[1])
        for i in range(2, n):
            res[i] = max(res[i - 2] + nums[i], res[i - 1])
        return res[-1]

    def rob3(self, nums):       # constant space
        n = len(nums)
        if n == 0:
            return 0
        if n <= 1:
            return max(nums)
        a, b = nums[0], max(nums[0], nums[1])
        for i in range(2, n):
            tmp = b
            b = max(a + nums[i], b)
            a = tmp
        return b


