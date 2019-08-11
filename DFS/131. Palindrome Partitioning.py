#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""====================================
# @Time    : 2019/8/11 21:20
# @Author  : Jing
# @FileName: 131. Palindrome Partitioning.py
# @IDE: PyCharm
======================================="""
# https://leetcode.com/problems/palindrome-partitioning/


class Solution:
    def recursion(self, s, start_index, strings, results):
        if start_index == len(s):
            results.append([i for i in strings])
            return

        for  i in range(start_index, len(s)):
            sub_s = s[start_index: i+1]
            if sub_s != sub_s[::-1]:
                continue
            strings.append(sub_s)
            self.recursion(s, i+1, strings, results)
            strings.pop()

    def partition(self, s):
        strings, results = [], []
        self.recursion(s, 0, strings, results)
        return results


if __name__ == '__main__':
    a = "aab"
    s = Solution()
    print(s.partition(a))               # Output is [['a', 'a', 'b'], ['aa', 'b']].

