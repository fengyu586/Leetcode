#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""====================================
# @Time    : 2019/8/15 17:33
# @Author  : Jing
# @FileName: 354. Russian Doll Envelopes.py
# @IDE: PyCharm
======================================="""
# https://leetcode.com/problems/russian-doll-envelopes/
# Solution 1: O(n^2)Time O(n)Space


class Solution:
    def maxEnvelopes(self, envelopes):
        if not envelopes:
            return 0
        envelopes = sorted(envelopes, key=lambda x: x[0])
        n = len(envelopes)
        dp = [0]*n
        for i in range(n):
            dp[i] = 1
            for j in range(i):
                if  envelopes[i][0] > envelopes[j][0] and envelopes[i][1] > envelopes[j][1]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)



if __name__ == '__main__':
    a = [[5,4],[6,4],[6,7],[2,3]]
    s = Solution()
    print(s.maxEnvelopes(a))                # Output is 3.