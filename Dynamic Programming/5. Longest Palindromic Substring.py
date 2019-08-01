#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""====================================
# @Time    : 2019/8/1 23:44
# @Author  : Jing
# @FileName: 5. Longest Palindromic Substring.py
# @IDE: PyCharm
======================================="""
# https://leetcode.com/problems/longest-palindromic-substring/


class Solution:

    def longestPalindrome0(self, s):
        n = len(s)
        dp = [[False for _ in range(n)] for _ in range(n)]
        max_len, min_index = 0, 0
        for i in range(n):
            for j in range(i+1):
                dp[j][i], sub_len = (s[i]==s[j]) and (i-j < 2 or dp[j+1][i-1]), i-j+1
                if dp[j][i] and max_len < sub_len:
                    max_len, min_index = sub_len, j
        return s[min_index:min_index+max_len]

    def longestPalindrome1(self, s):
        res = [[False for _ in range(len(s))] for _ in range(len(s))]
        max_sublen = 0
        max_indice = (0,0)

        for j in range(len(s)):
            for i in range(j+1):
                res[i][j] = s[i] == s[j] and (j - i < 2 or res[i+1][j-1])
                if res[i][j] and max_sublen < j - i + 1:
                    max_sublen = j - i + 1
                    max_indice = (i,j)

        return s[max_indice[0]:max_indice[1]+1]

    def longestPalindrome2(self, s):
        lenS = len(s)
        if lenS <= 1: return s
        minStart, maxLen, i = 0, 1, 0
        while i < lenS:
            if lenS - i <= maxLen // 2: break
            j, k = i, i
            while k < lenS - 1 and s[k] == s[k + 1]: k += 1
            i = k + 1
            while k < lenS - 1 and j and s[k + 1] == s[j - 1]:  k, j = k + 1, j - 1
            if k - j + 1 > maxLen: minStart, maxLen = j, k - j + 1
        return s[minStart: minStart + maxLen]


if __name__ == '__main__':
    Input = "babad"
    Output = "bab"
    s = Solution()
    out = s.longestPalindrome2(Input)
    print(out)
