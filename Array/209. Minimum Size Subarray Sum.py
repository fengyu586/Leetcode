# -*- coding: utf-8 -*-
# @Author  : Jing
# @FileName: 209. Minimum Size Subarray Sum.py
# @IDE: PyCharm
# https://leetcode.com/problems/minimum-size-subarray-sum/
# Solution 1: O(n)Time O(1)Space


class Solution:
    def minSubArrayLen(self, s, nums):
        if not nums:
            return 0
        l, r = 0, 0
        res = len(nums), None
        cur = 0
        while r < len(nums):
            cur += nums[r]
            if cur < s:
                r += 1
                continue
            while l <= r and cur >= s:
                if r - l + 1 <= res[0]:
                    res = r - l + 1, cur
                cur -= nums[l]
                l += 1
            r += 1
        if res[1] is None:
            return 0
        else:
            return res[0]


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5]
    n = 15
    s = Solution()
    print(s.minSubArrayLen(n, nums))