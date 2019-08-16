#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""====================================
# @Time    : 2019/8/16 16:46
# @Author  : Jing
# @FileName: 132. Palindrome Partitioning II.py
# @IDE: PyCharm
======================================="""
# https://leetcode.com/problems/palindrome-partitioning-ii/
# Solution 1: O(n^2)Time O(n)Space.
# Solution 2: O(n^2)Time O(n)Space          faster than Solution 1.
# Solution 3:


class Solution:
    def minCut1(self, s):
        if not s:
            return 0
        n = len(s)
        dp = list(range(n+1))
        for i in range(1, n+1):
            for j in range(i):
                if s[j:i] == s[j:i][::-1]:
                    dp[i] = min(dp[j]+1, dp[i])
        return dp[n]-1


    def minCut2(self, s):
        if s == s[::-1]:
            return 0
        n = len(s)
        for i in range(1, n):
            if s[i:] == s[i:][::-1] and s[:i] == s[:i][::-1]:
                return 1
        dp = list(range(n+1))
        for i in range(1, n):
            for j in range(i):
                if s[j:i] == s[j:i][::-1]:
                    dp[i] = min(dp[i], dp[j]+1)
        return dp[n]-1


if __name__ == '__main__':
    a = "aab"
    s = Solution()
    print(s.minCut2(a))         # Output is 1
