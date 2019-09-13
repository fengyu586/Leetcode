# -*- coding: utf-8 -*-
# @Author  : Jing
# @FileName: 189. Rotate Array.py
# @IDE: PyCharm
# https://leetcode.com/problems/rotate-array/
# Solution 1: O(n)Time
# Solution 2: O(n)Time

class Solution:
    def rotate(self, nums, k):
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        count = 0
        start = 0
        while count < len(nums):
            flat = 1
            cur = start
            prev = nums[start]
            while start != cur or flat:
                flat = 0
                nxt = (cur + k) % len(nums)
                tmp = nums[nxt]
                nums[nxt] = prev
                cur = nxt
                prev = tmp
                count += 1
            start += 1
        return nums

    def rotate1(self, nums, k):
        """
        Do not return anything, modify nums in-place instead.
        """
        def helper(nums, start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        k %= len(nums)
        helper(nums, 0, len(nums)-1)
        helper(nums, 0, k-1)
        helper(nums, k, len(nums)-1)
        return nums


if __name__ == '__main__':
    s = Solution()
    nums = list(range(1, 8))
    k = 3
    print(s.rotate1(nums, k))            # Output is [5, 6, 7, 1, 2, 3, 4]

