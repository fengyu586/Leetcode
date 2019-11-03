# -*- coding: utf-8 -*-
# @Author  : Jing
# @FileName: 90. Subsets II.py
# @IDE: PyCharm
# https://leetcode.com/problems/subsets-ii/


class Solution:
    def __init__(self):
        self.res = []

    def helper(self, nums, index, path):
        self.res.append(path)
        for i in range(index, len(nums)):
            if i != index and nums[i] == nums[i-1]:
                continue
            self.helper(nums, i+1, path+nums[i:i+1])
        return

    def subsetsWithDup(self, nums):
        if not nums:
            return self.res
        nums = sorted(nums)
        self.helper(nums, 0, [])
        return self.res


if __name__ == '__main__':
    nums = [1, 2, 2]
    s = Solution()
    print(s.subsetsWithDup(nums))





