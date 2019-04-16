#!/usr/bin/python3.6
# -*- coding:utf-8 -*-
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/


class Solution:
    def findMin0(self, nums):
        low, high = 0, len(nums)-1
        while low<high:
            mid = low +(high-low)//2
            if nums[mid]>=nums[mid+1]:
                return nums[mid+1]
            if nums[mid]<=nums[mid-1]:
                return nums[mid]
            if nums[mid]>nums[0]:
                low = mid+1
            else:
                high = mid-1
        return nums[0]

    def findMin1(self, nums):
        lo, hi = 0, len(nums)-1
        if nums[lo] < nums[hi]:
            return nums[lo]         # 递增
        while hi-lo > 1:
            mid = lo+(hi-lo)//2
            if nums[lo] > nums[mid]:
                hi = mid
            elif nums[hi] < nums[mid]:
                lo = mid
            else:
                lo += 1
        return nums[hi]



