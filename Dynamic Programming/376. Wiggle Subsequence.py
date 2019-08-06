#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""====================================
# @Time    : 2019/8/6 22:12
# @Author  : Jing
# @FileName: 376. Wiggle Subsequence.py
# @IDE: PyCharm
======================================="""
# https://leetcode.com/problems/wiggle-subsequence/
# Solution 1: Dynamic Programming: Time complexity : O(n^2) Space complexity : O(n)
# Solution 2:  Linear Dynamic Programming: Time complexity : O(n) Space complexity : O(n).
# Solution 3: Space-Optimized Dynamic Programming: Time complexity : O(n) Space complexity : O(1)
# Solution 4: Greedy Approach: Time complexity : O(n) Space complexity : O(1)


class Solution:
    def wiggleMaxLength1(self, nums):           # Time complexity : O(n^2). Loop inside a loop.
        n = len(nums)                           # Space complexity : O(n).
        if n < 2:                               # Two arrays of the same length are used for dp.
            return n
        up = [0 for i in range(n)]
        down = [0 for i in range(n)]
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    up[i] = max(up[i], down[j]+1)
                elif nums[i] < nums[j]:
                    down[i] = max(down[i], up[j]+1)
        return 1+max(down[-1], up[-1])

    def wiggleMaxLength2(self, nums):           # Time complexity : O(n). Loop inside a loop.
        n = len(nums)                           # Space complexity : O(n).
        if n < 2:                               # Two arrays of the same length are used for dp.
            return n
        up = [1 for _ in range(n)]
        down = [1 for _ in range(n)]
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                up[i] = down[i - 1] + 1
                down[i] = down[i - 1]
            elif nums[i] < nums[i - 1]:
                down[i] = up[i - 1] + 1
                up[i] = up[i - 1]
            else:
                down[i] = down[i - 1]
                up[i] = up[i - 1]
        return max(down[-1], up[-1])

    def wiggleMaxLength3(self, nums):           # Time complexity : O(n). Loop inside a loop.
        n = len(nums)                           # Space complexity : O(1).
        if n < 2:                               # Two arrays of the same length are used for dp.
            return n
        up = 1
        down = 1
        for i in range(1, n):
            if nums[i - 1] > nums[i]:
                down = up + 1
            elif nums[i - 1] < nums[i]:
                up = down + 1
        return max(up, down)

    def wiggleMaxLength4(self, nums):
        n = len(nums)
        if n < 2:
            return n
        pre_diff = nums[1] - nums[0]
        res = 1 if pre_diff == 0 else 2
        for i in range(2, n):
            diff = nums[i] - nums[i - 1]
            if diff * pre_diff < 0 or (pre_diff == 0 and diff != 0):
                res += 1
                pre_diff = diff
        return res


if __name__ == '__main__':
    a = [1,7,4,9,2,5]
    s = Solution()
    print(s.wiggleMaxLength1(a))        # Output is 6