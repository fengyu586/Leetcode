#!/usr/bin/python3.6
# -*- coding:utf-8 -*-
# https://leetcode.com/problems/decode-ways/
# 分治法：两个两个考虑


class Solution:
    def numDecodings(self, s):
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


if __name__ == '__main__':
    s = Solution()
    a = '226'
    print(s.numDecodings(a))
