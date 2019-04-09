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
        # more shorter
        try:
            left = nums.index(target)
            n = nums.count(target)
            return [left, left+n-1]
        except ValueError:
            return [-1, -1]

    def searchRange3(self, nums, target):
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

    # def searchRange4(self, nums, target):
    #     def searchRight(nums, target, low, high):
    #         while low < high:
    #             mid = low + (high-low)//2
    #             if mid != 0 and mid != len(nums)-1 and nums[mid-1] < target or nums[mid+1] > target and nums[mid] != target:
    #                 return -1
    #             if (mid == 0 or(mid > 0 and nums[mid-1] != target)) and nums[mid] == target:
    #                 return mid
    #             elif nums[mid] > target:
    #                 high = mid - 1
    #             else:
    #                 low = mid + 1
    #
    #         def searchLeft(nums, target, low, high):
    #             while


if __name__ == '__main__':
    # s = Solution()
    # num = [1, 2]
    # goal = 0
    # print(s.searchRange3(num, goal))
    l, r = [0, 1], [-1, 2]
    if -1 in l+r:
        a = max(l, r)
        print(a)
    else:
        print([l[0], r[1]])



