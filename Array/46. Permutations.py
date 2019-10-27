# -*- coding: utf-8 -*-
# @Author  : Jing
# @FileName: 46. Permutations.py
# @IDE: PyCharm
# https://leetcode.com/problems/permutations/
# Solution 1: backtrack
# Solution 2: DFS


class Solution:
    def __init__(self):
        self.res = []

    def generate1(self, nums, index):
        if index == len(nums):
            self.res.append([i for i in nums])
            return
        for i in range(index, len(nums)):
            nums[index], nums[i] = nums[i], nums[index]
            self.generate1(nums, index+1)
            nums[index], nums[i] = nums[i], nums[index]
        return

    def permute1(self, nums):
        if not nums:
            return nums
        index = 0
        self.generate1(nums, index)
        return self.res

    def generate2(self, nums, cur):
        if len(nums) == 1:
            self.res.append(cur+nums)
            return
        for i in range(len(nums)):
            new_nums = nums[:i] + nums[i + 1:]
            self.generate2(new_nums, cur+[nums[i]])


    def permute2(self, nums):
        if not nums:
            return nums
        self.generate2(nums, [])
        return self.res


if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    s = Solution()
    print(s.permute2(nums))

