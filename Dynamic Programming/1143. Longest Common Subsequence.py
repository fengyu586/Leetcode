# -*- coding: utf-8 -*-
# @Author  : Jing
# @FileName: 1143. Longest Common Subsequence.py
# @IDE: PyCharm
# https://leetcode.com/problems/longest-common-subsequence/
# Solution : DP     O(mn)Time O(mn)Space
# dp[i][j] denotes the length
# between the char of before ith char in text1
# and the char of before jth char in text1


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        if m * n == 0:
            return 0
        dp = [[0 for _ in range(n+1)] for i in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[m][n]


if __name__ == '__main__':
    str1, str2 = 'abcde', 'ace'
    s = Solution()
    print(s.longestCommonSubsequence(str1, str2))


