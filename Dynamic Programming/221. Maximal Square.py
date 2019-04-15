#!/usr/bin/python3.6
# -*- coding:utf-8 -*-
# https://leetcode.com/problems/maximal-square/


class Solution:
    def maximalSquare1(self, matrix):
        if not (matrix):
            return 0
        m, n = len(matrix), len(matrix[0])
        dp = [[0 for _ in range(n)] for __ in range(m)]
        max_val = 0
        for row in range(m):
            for col in range(n):
                if row == 0 or col == 0:
                    dp[row][col] = int(matrix[row][col])
                    max_val = max(max_val, dp[row][col])
                elif matrix[row][col] == '1':
                    dp[row][col] = min(dp[row - 1][col], dp[row - 1][col - 1], dp[row][col - 1]) + 1
                    max_val = max(max_val, dp[row][col])
        return max_val ** 2

    def maximalSquare2(self, matrix):
        if not (matrix):
            return 0
        m, n = len(matrix), len(matrix[0])
        max_val, prev = 0, 0
        dp = [0 for _ in range(n + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                tmp = dp[j]
                if matrix[i - 1][j - 1] == '1':
                    dp[j] = min(dp[j - 1], dp[j], prev) + 1
                    max_val = max(max_val, dp[j])
                else:
                    dp[j] = 0
                prev = tmp
        return max_val ** 2


def main():
    martix = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]
    s = Solution()
    print(s.maximalSquare2(martix))


if __name__ == '__main__':
    main()

