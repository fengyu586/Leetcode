# -*- coding: utf-8 -*-
# @Author  : Jing
# @FileName: 1218. Longest Arithmetic Subsequence of Given Difference.py
# @IDE: PyCharm
# https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/


class Solution:
    def longestSubsequence(self, arr, difference: int) -> int:
        if not arr:
            return 0
        dic = {}
        for i, num in enumerate(arr):
            dic[num] = dic.get(num-difference, 0) + 1
        return max(dic.values())


if __name__ == '__main__':
    s = Solution()
    nums, difference = [1, 2, 3, 4], 1
    print(s.longestSubsequence(nums, difference))



