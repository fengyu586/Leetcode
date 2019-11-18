# -*- coding: utf-8 -*-
# @Author  : Jing
# @FileName: 162. Find Peak Element.py
# @IDE: PyCharm
# https://leetcode.com/problems/find-peak-element/
# Solution 1: iteratively   O(logn)Time     O(1)Space
# Solution 2: recursively   O(logn)Time     O(logn)Space

class Solution:
    def findPeakElement1(self, nums):
        if not nums:
            return -1
        l, r = 0, len(nums) - 1
        nums.append(float("-inf"))
        while l < r:
            mid = (l+r) >> 1
            if nums[mid] < nums[mid+1]:
                l = mid + 1
            else:
                r = mid
        return l

    def helper(self, nums, l, r):
        if l == r:
            return l
        if l < r:
            mid = (l+r) >> 1
            if nums[mid] < nums[mid+1]:
                l = mid+1
            else:
                r = mid
            return self.helper(nums, l, r)

    def findPeakElement2(self, nums):
        if not nums:
            return -1
        l, r = 0, len(nums)
        nums.append(float("-inf"))
        return self.helper(nums, l ,r)



if __name__ == '__main__':
    nums = [1, 2, 3, 1]
    s = Solution()
    print(s.findPeakElement2(nums))

