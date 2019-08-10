#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""====================================
# @Time    : 2019/8/10 22:20
# @Author  : Jing
# @FileName: 123. Best Time to Buy and Sell Stock III.py
# @IDE: PyCharm
======================================="""


class Solution:
    def maxProfit(self, prices):
        n = len(prices)
        if n == 0:
            return 0
        dp = [[0.0 for _ in range(5 + 1)] for i in range(n + 1)]
        # the first day, phase 1, max profit = 0
        dp[0][1] = 0
        for i in range(2, 6):
            dp[0][i] = float('-inf')
        for i in range(1, n + 1):
            for j in range(1, 6, 2):
                dp[i][j] = dp[i - 1][j]
                if j > 1 and i > 1 and dp[i - 1][j - 1] != float('-inf'):
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + prices[i - 1] - prices[i - 2])
            for j in range(2, 6, 2):
                dp[i][j] = dp[i - 1][j - 1]
                if i > 1 and dp[i - 1][j] != float('-inf'):
                    dp[i][j] = max(dp[i][j], dp[i - 1][j] + prices[i - 1] - prices[i - 2])

                if j > 2 and i > 1 and dp[i - 1][j - 2] != float('-inf'):
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - 2] + prices[i - 1] - prices[i - 2])
        return max(dp[n][1], dp[n][3], dp[n][5])


if __name__ == '__main__':
    a = [3,3,5,0,0,3,1,4]
    s = Solution()
    print(s.maxProfit(a))               # Output is 6





