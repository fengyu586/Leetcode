#!/usr/bin/python3.6
# -*- coding:utf-8 -*-
# https://leetcode.com/problems/counting-bits/


class Solution:
    def countBits(self, num):
        dp = [0]*(num+1)
        if num == 0:
            return dp
        ind = 0
        for i in range(1, num+1):
            if i-1 != 0 and i & (i-1) == 0:
                ind = 0
            dp[i] = dp[ind]+1
            ind += 1
        return dp


def main():
    s = Solution()
    n = 16
    print(s.countBits(n))


if __name__ == '__main__':
    main()


