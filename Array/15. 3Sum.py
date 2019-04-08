#!/usr/bin/python3.6
# -*- coding:utf-8 -*-
# https://leetcode.com/problems/3sum/
# tips: 1、先排序 2、利用字典降低时间复杂度


class Solution:
    def threeSum1(self, nums):
        n = len(nums)
        nums.sort()
        res = []
        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            first, end = i+1, n-1
            while first < end:
                s = nums[i]+nums[first]+nums[end]
                if s < 0:
                    first += 1
                elif s > 0:
                    end -= 1
                else:
                    res.append([nums[i], nums[first], nums[end]])
                    while first < end and nums[first] == nums[first+1]:
                        first += 1
                    while first < end and nums[end] == nums[end-1]:
                        end -= 1
                    first += 1
                    end -= 1
        return res

    def threeSum2(self, nums):
        n = len(nums)
        if n < 3:
            return []
        nums.sort()
        res = set()
        for i, v in enumerate(nums[:-2]):
            if i > 0 and v == nums[i - 1]:
                continue
            d = {}
            for x in nums[i + 1:]:
                if x not in d:
                    d[-v - x] = 1
                else:
                    res.add((v, -v - x, x))
        return list(map(list, res))
