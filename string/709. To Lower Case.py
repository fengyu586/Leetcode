# -*- coding: utf-8 -*-
# @Author  : Jing
# @FileName: 709. To Lower Case.py
# @IDE: PyCharm
# https://leetcode.com/problems/to-lower-case/


class Solution:
    def toLowerCase(self, string):
        if not string:
            return string
        string = list(string)
        n = len(string)
        distance = ord('a')-ord('A')
        for i in range(n):
            if 'A' <= string[i] and string[i] < 'a':
                string[i] = chr(ord(string[i])+distance)
        return ''.join(string)


if __name__ == '__main__':
    string = 'Hello'
    s = Solution()
    print(s.toLowerCase(string))


