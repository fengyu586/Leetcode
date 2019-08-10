#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""====================================
# @Time    : 2019/8/10 16:30
# @Author  : Jing
# @FileName: 674. Longest Continuous Increasing Subsequence.py
# @IDE: PyCharm
======================================="""
# https://leetcode.com/problems/longest-continuous-increasing-subsequence/
# Solution 1: O(n) Time and O(n) Space
# Solution 2: O(n) Time and O(1) Space


class Solution:
    def findLengthOfLCIS1(self, nums):
        n = len(nums)
        if n == 0:
            return 0
        res = [1] * n
        for i in range(n):
            if i > 0 and nums[i] > nums[i - 1]:
                res[i] = res[i - 1] + 1
        return max(res)

    def findLengthOfLCIS2(self, nums):
        n = len(nums)
        if n == 0:
            return 0
        res = 1
        max_val = 1
        for i in range(n):
            if i > 0 and nums[i] > nums[i - 1]:
                res += 1
            else:
                res = 1
            max_val = max(max_val, res)
        return max_val


if __name__ == '__main__':
    a = [1,3,5,4,7]
    s = Solution()
    print(s.findLengthOfLCIS1(a))           # Output is 3