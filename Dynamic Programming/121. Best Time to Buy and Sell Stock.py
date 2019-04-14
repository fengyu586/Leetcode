#!/usr/bin/python3.6
# -*- coding:utf-8 -*-
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/


class Solution:
    def maxProfit1(self, prices):
        import sys
        min_price = sys.maxsize
        max_profit = 0
        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            else:
                max_profit = max(prices[i]-min_price, max_profit)
        return max_profit

    def maxProfit2(self, prices):
        if not prices:
            return 0
        loc = glo = 0
        for i in range(1, len(prices)):
            loc = max(loc + prices[i] - prices[i - 1], 0)
            glo = max(glo, loc)
        return glo

    def maxProfit3(self, prices):
        if not prices:
            return 0
        minPri, maxPro = prices[0], 0
        for i in range(1, len(prices)):
            minPri = min(minPri, prices[i])
            maxPro = max(maxPro, prices[i] - minPri)
        return maxPro




