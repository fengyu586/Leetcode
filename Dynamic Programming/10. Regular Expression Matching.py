#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""====================================
# @Time    : 2019/8/2 20:36
# @Author  : Jing
# @FileName: 10. Regular Expression Matching.py
# @IDE: PyCharm
======================================="""
# https://leetcode.com/problems/regular-expression-matching/
# Solution 1: Recursion
# Solution 2: Dynamic Programming


class Solution:
    def isMatch0(self, s, p):
        if not p:
            return not s

        first_match = bool(s) and p[0] in {s[0], '.'}

        if len(p) >= 2 and p[1] == '*':         # * denote 0
            return (self.isMatch0(s, p[2:]) or
                    first_match and self.isMatch0(s[1:], p))            # * denote more
        else:
            return first_match and self.isMatch0(s[1:], p[1:])          # p does not contain *

    def isMatch(self, s, p):
        T = [[True] + [False] * len(p)] + [[False] * (len(p) + 1) for _ in range(len(s))]
        s, p = ' ' + s, ' ' + p
        for i in range(len(T)):
            for j in range(1, len(T[0])):
                if p[j] == '*':
                    if i == 0 or T[i][j - 2]:  # zero of the character before *
                        T[i][j] = T[i][j - 2]
                    elif i > 0 and (s[i] == p[j - 1] or p[j - 1] == '.'):  # one or more of the characters before *
                        T[i][j] = T[i - 1][j]
                elif i > 0 and (s[i] == p[j] or p[j] == '.'):  # exact match at i and j or a '.'
                    T[i][j] = T[i - 1][j - 1]
        return T[-1][-1]


if __name__ == '__main__':
    s = Solution()
    a = 'aaa'
    b = 'a*'
    print(s.isMatch(a, b))

