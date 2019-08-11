#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""====================================
# @Time    : 2019/8/11 22:05
# @Author  : Jing
# @FileName: 215. Kth Largest Element in an Array.py
# @IDE: PyCharm
======================================="""
# https://leetcode.com/problems/kth-largest-element-in-an-array/
# Solution 1: O(nlogn) Time
# Solution 2: O(nk) Time
# Solution 3: O(n) Time


class Solution:
    def quick_select(self, nums, start, end, k):
        if start == end:
            return nums[start]
        i, j = start, end
        tmp = nums[(i+j)//2]
        while i <= j:
            while i <= j and nums[i] > tmp:
                i += 1
            while i <= j and nums[j] < tmp:
                j -= 1
            if i <= j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
        if start + k  - 1 <= j:
            return self.quick_select(nums, start, j, k)
        if start +k -1 >= i:
            return self.quick_select(nums, i, end, k - (i - start))
        return nums[j+1]


    def findKthLargest1(self, nums, k):
        if not nums:
            return None
        nums = sorted(nums, reverse=True)
        return nums[k-1]

    def findKthLargest2(self, nums, k):
        if not nums:
            return None
        n = len(nums)
        for i in range(k):
            for j in range(i+1, n):
                if nums[j] > nums[i]:
                    nums[j], nums[i] = nums[i], nums[j]
        return nums[k-1]

    def findKthLargest3(self, nums, k):
        if not nums:
            return None
        return self.quick_select(nums, 0, len(nums)-1, k)


if __name__ == '__main__':
    a = [3,2,3,1,2,4,5,5,6]
    k = 4
    s = Solution()
    print(s.findKthLargest3(a, k))               # Output is 4.
