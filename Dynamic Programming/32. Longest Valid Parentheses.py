#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""====================================
# @Time    : 2019/8/7 20:48
# @Author  : Jing
# @FileName: 32. Longest Valid Parentheses.py
# @IDE: PyCharm
======================================="""
# https://leetcode.com/problems/longest-valid-parentheses/
# Solution 1: stack
# Solution 2: dp


class Solution:
    def longestValidParentheses1(self, s):
        s = ")" + s
        stack, ans = [], 0
        for index in range(len(s)):
          element = s[index]
          if element == ")" and stack and stack[-1][1] == "(":
              stack.pop()
              ans = max(ans, index - stack[-1][0])
          else:
            stack.append((index, element))
        return ans


if __name__ == '__main__':
    string = ")()()"
    S = Solution()
    print(S.longestValidParentheses1(string))
