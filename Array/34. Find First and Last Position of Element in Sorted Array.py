#!/usr/bin/python3.6
# -*- coding:utf-8 -*-
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
# 1.linear scope 2. binary search


class Solution:
    def searchRange1(self, nums, target):
        # linear scan
        n = len(nums)
        res = []
        for i in range(n):
            if target == nums[i]:           # the goal is find the staring and ending position of a given target value
                if len(res) < 2:
                    res += [i]
                else:
                    res[-1] = i
        if not(res):
            return [-1, -1]
        elif len(res) == 1:
            return res*2
        else:
            return res

    def searchRange2(self, nums, target):
        # binary search
        if target not in nums:
            return [-1, -1]
        n = len(nums)
        l, r = 0, n - 1
        while l < r:
            if nums[l] != target:
                l += 1
            if nums[r] != target:
                r -= 1
            if nums[l] == target and nums[r] == target:
                break




