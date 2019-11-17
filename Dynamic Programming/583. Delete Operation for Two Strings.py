# -*- coding: utf-8 -*-
# @Author  : Jing
# @FileName: 583. Delete Operation for Two Strings.py
# @IDE: PyCharm
# https://leetcode.com/problems/delete-operation-for-two-strings/
# Solution 1: DP    O(mn)Time   O(mn)Space
# Solution 2: DP    O(mn)Time   O(n)Space


class Solution:
    def minDistance1(self, word1: str, word2: str) -> int:
            m, n = len(word1), len(word2)
            if m*n == 0:
                return m+n
            dp = [[0 for _ in range(n+1)] for i in range(m+1)]
            for i in range(m+1):
                dp[i][0] = i
            for i in range(n+1):
                dp[0][i] = i
            for i in range(1, m+1):
                for j in range(1, n+1):
                    if word1[i-1] != word2[j-1]:
                        dp[i][j] = min(dp[i][j-1], dp[i-1][j]) + 1
                    else:
                        dp[i][j] = dp[i-1][j-1]
            return dp[m][n]

    def minDistance2(self, word1, word2):
        m, n = len(word1), len(word2)
        if m*n == 0:
            return m + n
        dp = [[i for i in range(n+1)] for _ in range(2)]
        for i in range(1, m+1):
            index = i % 2
            for j in range(n+1):
                if j == 0:
                    dp[index][j] = i
                    continue
                if word1[i-1] != word2[j-1]:
                    dp[index][j] = min(dp[(i-1)%2][j], dp[index][j-1]) + 1
                else:
                    dp[index][j] = dp[(i-1)%2][j-1]
        return dp[m%2][n]


if __name__ == '__main__':
    str1, str2 = 'sea', 'eat'
    s = Solution()
    print(s.minDistance2(str1, str2))


