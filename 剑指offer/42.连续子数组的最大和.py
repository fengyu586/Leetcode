# -*- coding: utf-8 -*-
# @Author  : Jing
# @FileName: 42.连续子数组的最大和.py
# @IDE: PyCharm
# Solution 1: DP O(n)Time O(n)Space
# Solution 2: O(n)Time O(1)Space


class Solution:
    def FindGreatestSumOfSubArray1(self, nums):
        if not nums:
            return 0
        n = len(nums)
        dp = [nums[0] for _ in range(n)]
        for i in range(1, n):
            if dp[i-1] <= 0:
                dp[i] = nums[i]
            else:
                dp[i] = dp[i-1] + nums[i]
        return max(dp)

    def FindGreatestSumOfSubArray2(self, nums):
        if not nums:
            return 0
        n = len(nums)
        max_val = 0
        res = float("-inf")
        for i in range(n):
            max_val += nums[i]
            if max_val > res:
                res = max_val
            if max_val <= 0:
                max_val = 0
        return res


if __name__ == '__main__':
    s = Solution()
    nums = [1, -2, 3, 10, -4, 7, 2, -5]
    print(s.FindGreatestSumOfSubArray1(nums))


