#!/usr/bin/python3.6
# -*- coding:utf-8 -*-
# https://leetcode.com/problems/min-cost-climbing-stairs/
# two Approaches


class Solution:
    def minCostClimbingStairs1(self, cost):
        f1, f2 = 0, 0
        for i in range(len(cost)-1, -1, -1):
            f1, f2 = cost[i] + min(f1, f2), f1
        return min(f1, f2)

    def minCostClimbingStairs2(self, cost):
        n = len(cost)
        res = [0] * n
        for i in range(2, n):
            res[i] = min(res[i - 1] + cost[i - 1], res[i - 2] + cost[i - 2])
        return min(res[-1] + cost[-1], res[-2] + cost[-2])


def main():
    s = Solution()
    a = [0, 0, 1, 1]
    print(s.minCostClimbingStairs2(a))


if __name__ == '__main__':
    main()


