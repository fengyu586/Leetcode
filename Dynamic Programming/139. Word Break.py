#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""====================================
# @Time    : 2019/8/9 15:29
# @Author  : Jing
# @FileName: 139. Word Break.py
# @IDE: PyCharm
======================================="""
# https://leetcode.com/problems/word-break/


class Solution:
    def wordBreak(self, s, wordDict):
        n = len(s)
        dp = [False]*(n+1)
        dp[0] = True
        for i in range(1, n+1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[-1]


if __name__ == '__main__':
    a = "applepenapple"
    wordDict = ["apple", "pen"]
    s = Solution()
    print(s.wordBreak(a, wordDict))



