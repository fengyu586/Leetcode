#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""====================================
# @Time    : 2019/8/15 16:12
# @Author  : Jing
# @FileName: 188. Best Time to Buy and Sell Stock IV.py
# @IDE: PyCharm
======================================="""
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/
# Solution 1: O(NK)Time, O(NK)Space


class Solution:
    def maxProfit(self, k, prices):
        if not prices:
            return 0
        n = len(prices)
        if k >= n:
            res = 0
            for i in range(n-1):
                res += max(prices[i+1]-prices[i], 0)
            return res
        dp = [[0.0 for i in range(2*k+2)] for _ in range(n+1)]
        for i in range(2, 2*k+2):
            dp[0][i] = float('-inf')
        for i in range(1, n+1):
            for j in range(1, 2*k+2, 2):
                dp[i][j] = dp[i-1][j]
                if i>1 and j>1 and dp[i-1][j-1] != float('-inf'):
                    dp[i][j] = max(dp[i][j], dp[i-1][j-1]+prices[i-1]-prices[i-2])
            for j in range(2, 2*k+2, 2):
                dp[i][j] = dp[i-1][j-1]
                if i>1 and dp[i-1][j] != float('-inf'):
                    dp[i][j] = max(dp[i][j], dp[i-1][j]+prices[i-1]-prices[i-2])
                if i>1 and j > 2 and dp[i-1][j-2] != float('inf'):
                    dp[i][j] = max(dp[i][j], dp[i-1][j-2]+prices[i-1]-prices[i-2])
        return int(max([dp[n][i] for i in range(1, 2*k+2, 2)]))


if __name__ == '__main__':
    prices = [2,4,1]
    k = 2
    s = Solution()
    print(s.maxProfit(k, prices))               # Output is 2.


