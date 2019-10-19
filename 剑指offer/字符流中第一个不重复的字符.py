# -*- coding: utf-8 -*-
# @Author  : Jing
# @FileName: 字符流中第一个不重复的字符.py
# @IDE: PyCharm


class Solution:
    def __init__(self):
        self.s = ''
        self.dic = dict()

    def FirstAppearingOnce(self):
        for s in self.s:
            if self.dic[s] == 1:
                return s
        return '#'

    def Insert(self, char):
        self.s += char
        if char in self.dic:
            self.dic[char] += 1
        else:
            self.dic[char] = 1


if __name__ == '__main__':
    s = Solution()
    for i in range(10):
        s.Insert(str(i))
    print(s.FirstAppearingOnce())

