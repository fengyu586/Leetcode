#!/usr/bin/python3.6
# -*- coding:utf-8 -*-
# https://leetcode.com/problems/3sum-closest/
# tips: 1.two pointer


class Solution:
    def threeSumClosest(self, nums, target):
        n = len(nums)
        nums.sort()
        res = sum(nums[:3])
        for i in range(n-1):
            l, r = i+1, n-1
            while l < r:
                s = nums[i]+nums[l]+nums[r]
                if abs(s-target) < abs(res-target):
                    res = s
                elif s < target:
                    l += 1
                elif s > target:
                    r -= 1
                else:
                    return res
        return res




