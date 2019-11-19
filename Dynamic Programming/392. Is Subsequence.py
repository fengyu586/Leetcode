# -*- coding: utf-8 -*-
# @Author  : Jing
# @FileName: 392. Is Subsequence.py
# @IDE: PyCharm
# https://leetcode.com/problems/is-subsequence/


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        index = 0
        for item in t:
            if s[index] == item:
                index += 1
            if index == len(s):
                return True
        return False


if __name__ == '__main__':
    string, t = 'abc', 'ahbgdc'
    s = Solution()
    print(s.isSubsequence(string, t))
