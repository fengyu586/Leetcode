#!/usr/bin/python3.6
# -*- coding:utf-8 -*-
# https://leetcode.com/problems/decode-ways/
# Approach1: 分治法：两个两个考虑, 时间复杂度：O(n)，空间复杂度：O(1)
# Approach2: 时间复杂度：O(n)， 空间复杂度：O(n)


class Solution:
    def numDecodings1(self, s):
        if not s or s == '0':
            return 0
        n = len(s)
        if n == 1:
            return 1
        merge, done = 0, 1
        for i in range(1, n):
            l, r = s[i-1], s[i]
            if r == '0':
                if l != '1' and l != '2':
                    return 0
                else:
                    merge, done = done, 0
            elif l == '0':
                merge, done = 0, merge
            else:
                if 10 < int(l+r) < 27:
                    merge, done = done, merge + done
                else:
                    merge, done = 0, merge+done
        return merge+done

    def numDecodings2(self, s):
        if not s:
            return 0
        n = len(s)
        dp = [1] + [0] * n
        for i in range(1, n + 1):
            if s[i - 1] != '0':
                dp[i] += dp[i - 1]
            if i > 1 and 10 <= int(s[i - 2: i]) <= 26:
                dp[i] += dp[i - 2]
        return dp[n]


if __name__ == '__main__':
    s = Solution()
    a = '226'
    print(s.numDecodings2(a))
