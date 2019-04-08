#!/usr/bin/python3.6
# -*- coding:utf-8 -*-
# https://leetcode.com/problems/4sum/
# could compute N Sum
# tips: 先拆成找2个数的和


class Solution:
    def findNSum(self, nums, target, N, result, results):
        if len(nums) < N or N < 2 or target < nums[0] * N or target > nums[-1] * N:
            return
        n = len(nums)
        if N == 2:
            l, r = 0, n - 1
            while l < r:
                s = nums[l] + nums[r]
                if s < target:
                    l += 1
                elif s > target:
                    r -= 1
                else:
                    results.append(result + [nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
        else:
            for i in range(n - N + 1):
                if i == 0 or (i > 0 and nums[i] != nums[i - 1]):
                    self.findNSum(nums[i + 1:], target - nums[i], N - 1, result + [nums[i]], results)
            return

    def fourSum(self, nums, target):
        nums.sort()
        results = []
        self.findNSum(nums, target, 4, [], results)
        return results
