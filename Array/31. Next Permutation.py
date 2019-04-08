#!/usr/bin/python3.6
# -*- coding:utf-8 -*-
# https://leetcode.com/problems/next-permutation/


class Solution:
    def nextPermutation(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        m = n = len(nums)-1
        while m > 0 and nums[m-1] >= nums[m]:        # find first descend number
            m -= 1
        if m == 0:
            nums.sort()
            return
        m -= 1
        while n > m and nums[n] <= nums[m]:         # find last ascend number
            n -= 1
        nums[m], nums[n] = nums[n], nums[m]
        l, r = m+1, len(nums)-1
        while l < r:                                # reverse the part of nums[m+1:]
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l+1, r-1
        return


if __name__ == '__main__':
    s = Solution()
    nums = [1, 2]
    s.nextPermutation(nums)
    # print(nums)



