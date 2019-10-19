# -*- coding: utf-8 -*-
# @Author  : Jing
# @FileName: 20.表示数值的字符串.py
# @IDE: PyCharm
# Solution 1: Sequential traversal O(n)Time O(1)Space
# Solution 2: O(1)Time O(1)Space


class Solution:
    def isInteger(self, s, start):
        n = len(s)
        while start < n and s[start].isdigit():
            start += 1
        if start == n:
            flag = True
        else:
            flag = False
        return start, flag

    def isSign(self, s, start):
        n = len(s)
        if start < n and (s[start] == "+" or s[start] == "-"):
            start += 1
        return start

    def isNumberic1(self, s):
        if not s:
            return None
        if s.endswith('e') or s.endswith('E'):
            return False
        start = 0
        start = self.isSign(s, start)
        start, flag = self.isInteger(s, start)
        if not flag and s[start] == ".":
            start += 1
            start, flag = self.isInteger(s,start)
            if not flag:
                if s[start] == "E" or s[start] == "e":
                    start += 1
                    start = self.isSign(s, start)
                    start, flag = self.isInteger(s, start)
        elif not flag and (s[start] == "E" or s[start] == "e"):
            start += 1
            start = self.isSign(s, start)
            start, flag = self.isInteger(s, start)
        return flag

    def isNumberic2(self, s):
        if not s:
            return None
        if s.endswith("e") or s.endswith("E"):
            return False
        try:
            float(s)
            return True
        except:
            return False


if __name__ == '__main__':
    string = "12.54e"
    s = Solution()
    print(s.isNumberic2(string))

