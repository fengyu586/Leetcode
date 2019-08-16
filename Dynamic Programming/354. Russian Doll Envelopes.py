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
# Solution 2: O(nlogn)Time O(n)Space


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

    def maxEnvelopes0(self, envelopes):
        size = len(envelopes)
        # 特判
        if size < 2:
            return size

        # 对第一列排序，按照宽度排序
        # 【特别注意】当宽度相等的时候，按照高度降序排序
        # 以避免 [[11, 3], [12, 4], [12, 5], [12, 6], [14, 6]] 这种情况发生
        # 正确排序 [[11, 3], [12, 6], [12, 5], [12, 4], [14, 6]]
        envelopes.sort(key=lambda x: (x[0], -x[1]))

        # print(envelopes)
        tail = [envelopes[0][1]]

        for i in range(1, size):
            target = envelopes[i][1]
            if target > tail[-1]:
                tail.append(target)
                continue

            left = 0
            right = len(tail) - 1

            while left < right:
                mid = (left + right) >> 1
                if tail[mid] < target:
                    left = mid + 1
                else:
                    right = mid
            tail[left] = target
        # print(tail)
        return len(tail)

if __name__ == '__main__':
    a = [[1,2],[2,3],[3,4],[3,5],[4,5],[5,5],[5,6],[6,7],[7,8]]
    s = Solution()
    print(s.maxEnvelopes0(a))                # Output is 7.