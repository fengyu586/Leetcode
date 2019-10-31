# -*- coding: utf-8 -*-
# @Author  : Jing
# @FileName: 78. Subsets.py
# @IDE: PyCharm
# https://leetcode.com/problems/subsets/
# Solution 1: recursively
# Solution 2: iteratively


class Solution:
    def __init__(self):
        self.res = []

    def helper(self, nums, k, i, cur):
        if len(cur) == k:
            self.res.append(cur)
            return
        else:
            for j in range(i, len(nums)):
                self.helper(nums, k, j+1, cur + nums[j:j+1])

    def subsets1(self, nums):
        if not nums:
            return [[]]
        for k in range(len(nums) + 1):
            self.helper(nums, k, 0, [])
        return self.res

    def subsets2(self, nums):
        res = [[]]
        for i in range(len(nums)):
            res += [item+nums[i:i+1] for item in res]
        return res


if __name__ == '__main__':
    nums = [1, 2, 3]
    s = Solution()
    print(s.subsets2(nums))

