# -*- coding: utf-8 -*-
# @Author  : Jing
# @FileName: 290. Word Pattern.py
# @IDE: PyCharm
# https://leetcode.com/problems/word-pattern/


class Solution:
    def wordPattern(self, pattern, str):
        dic0 = {}
        dic1 = {}
        s = list(str.split())
        if len(s) != len(pattern):
            return False
        for i, p in enumerate(pattern):
            if p not in dic0:
                dic0[p] = s[i]
            if s[i] not in dic1:
                dic1[s[i]] = p
            if dic0[p] == s[i] and dic1[s[i]] == p:
                continue
            else:
                return False
        return True

    def wordPattern1(self, pattern, str):
        dic = {}
        s = list(str.split())
        if len(pattern) != len(s):
            return False
        p_set = set(pattern)
        for i in p_set:
            dic[i] = set()
        for i in range(len(s)):
            dic[pattern[i]].add(s[i])
        for val in dic.values():
            if len(val) != 1:
                return False
        return True


if __name__ == '__main__':
    s = Solution()
    pattern, strings = "abba", "dog cat cat fish"
    print(s.wordPattern1(pattern, strings))
