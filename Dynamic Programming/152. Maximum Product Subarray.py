#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""====================================
# @Time    : 2019/8/9 19:04
# @Author  : Jing
# @FileName: 152. Maximum Product Subarray.py
# @IDE: PyCharm
======================================="""
# https://leetcode.com/problems/maximum-product-subarray/
# Solution 1 : O(2*n) space
# Solution 2 : O(1) space
# Solution 3 : O(1) space


class Solution:
    def maxProduct1(self, nums):
        n = len(nums)
        locMin = [0]*n
        locMax = [0]*n
        locMin[0] = locMax[0] = gloMax = nums[0]
        for i in range(1, n):
            if nums[i] < 0:
                locMin[i] = min(locMax[i-1]*nums[i], nums[i])
                locMax[i] = max(locMin[i-1]*nums[i], nums[i])
            else:
                locMin[i] = min(locMin[i-1]*nums[i], nums[i])
                locMax[i] = max(locMax[i-1]*nums[i], nums[i])
        return max(locMax+[gloMax])

    def maxProduct2(self, nums):
        n = len(nums)
        locMin = locMax = gloMax = nums[0]
        for i in range(1, n):
            if nums[i] < 0:
                tmp = locMin
                locMin = min(locMax*nums[i], nums[i])
                locMax = max(tmp*nums[i], nums[i])
            else:
                locMin = min(locMin*nums[i], nums[i])
                locMax = max(locMax*nums[i], nums[i])
            gloMax = max(gloMax, locMax)
        return gloMax

    def maxProduct3(self, nums):
        if not nums:
            return
        n = len(nums)
        locMin = locMax = gloMax = nums[0]
        for i in range(1, n):
            tmp_li = [locMin * nums[i], nums[i], locMax * nums[i]]
            locMin = min(tmp_li)
            locMax = max(tmp_li)
            gloMax = max(gloMax, locMax)
        return gloMax


if __name__ == '__main__':
    nums = [2,3,-2,4]
    s = Solution()
    print(s.maxProduct1(nums))      # Output is 6



