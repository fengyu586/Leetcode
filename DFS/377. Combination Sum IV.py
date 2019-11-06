# -*- coding: utf-8 -*-
# @Author  : Jing
# @FileName: 377. Combination Sum IV.py
# @IDE: PyCharm
# https://leetcode.com/problems/combination-sum-iv/
# Solution 1: backtrace O(2^n)Time O(2^n)Space
# Solution 2: dp O(mn)Time O(m)Space


class Solution:
    def __init__(self):
        self.res = []

    def sub_sum(self, nums, remain_sum, path):
        if remain_sum == 0:
            if path not in self.res:
                self.res.append([i for i in path])
            return
        for i in range(len(nums)):
            num = nums[i]
            if num > remain_sum:
                break
            self.sub_sum(nums, remain_sum-num, path+[num])
        return

    def combinationSum41(self, nums, target):
        if not nums:
            return 0
        self.sub_sum(nums, target, [])
        return len(self.res)

    def combinationSum42(self, nums, target):
        if not nums:
            return 0
        dp = [0 for _ in range(target+1)]
        dp[0] = 1
        for i in range(1, target+1):
            for num in nums:
                if num <= i:
                    dp[i] += dp[i-num]
        return dp[target]


if __name__ == '__main__':
    nums = [1, 50]
    target = 200
    s = Solution()
    print(s.combinationSum42(nums, target))






