#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""====================================
# @Time    : 2019/8/10 20:36
# @Author  : Jing
# @FileName: 213. House Robber II.py
# @IDE: PyCharm
======================================="""
# https://leetcode.com/problems/house-robber-ii/
# Solution 1: O(N^2) Time and O(N) Space
# Solution 2: O(N^2) Time and O(1) Space
# Solution 3: O(N) Time and O(N) Space
# Solution 4: O(N) Time and O(1) Space


class Solution:
    def helper1(self, nums):
        n = len(nums)
        if n == 0:
            return 0
        res = [0] * (n + 1)
        res[1] = nums[0]
        for i in range(2, n + 1):
            res[i] = max(res[i - 1], res[i - 2] + nums[i - 1])
        return res[n]

    def helper2(self, nums):
        n = len(nums)
        if n == 0:
            return 0
        a, b = 0, nums[0]
        for i in range(2, n+1):
            a, b = b, max(b, a+nums[i-1])
        return b

    def rob1(self, nums):
        n = len(nums)
        if n == 0:
            return 0
        if n <= 3:
            return max(nums)
        dp = [0] * (n)
        for i in range(n):
            if i <= 1:
                dp[i] = nums[i] + self.helper1(nums[i + 2:n + i - 1])
            if 1 < i <= n - 3:
                dp[i] = nums[i] + self.helper1(nums[i + 2:n] + nums[0:i - 1])
            if i > n - 3:
                dp[i] = nums[i] + self.helper1(nums[i + 2 - n:i - 1])
        return max(dp)

    def rob2(self, nums):
        n = len(nums)
        if n == 0:
            return 0
        if n <= 3:
            return max(nums)
        dp = [0] * (n)
        for i in range(n):
            if i <= 1:
                dp[i] = nums[i] + self.helper2(nums[i + 2:n + i - 1])
            if 1 < i <= n - 3:
                dp[i] = nums[i] + self.helper2(nums[i + 2:n] + nums[0:i - 1])
            if i > n - 3:
                dp[i] = nums[i] + self.helper2(nums[i + 2 - n:i - 1])
        return max(dp)

    def rob3(self, nums):
        n = len(nums)
        if n == 0:
            return 0
        if n <= 3:
            return max(nums)
        return max(self.helper1(nums[:-1]), self.helper1(nums[1:]))

    def rob4(self, nums):
        n = len(nums)
        if n == 0:
            return 0
        if n <= 3:
            return max(nums)
        return max(self.helper2(nums[:-1]), self.helper2(nums[1:]))


if __name__ == '__main__':
    a = [1,2,3,1]
    s = Solution()
    print(s.rob4(a))



