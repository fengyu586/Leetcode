# -*- coding: utf-8 -*-
# @Author  : Jing
# @FileName: 58.翻转字符串.py
# @IDE: PyCharm


class Solution:
    def Reversed(self, s, start, end):
        if not s:
            return
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1
        return

    def ReverseSentence(self, s):
        if not s:
            return s
        s = list(s)
        self.Reversed(s, 0, len(s)-1)
        n = len(s)
        start = end = 0
        while start < n:
            if s[start] == " ":
                start += 1
                end += 1
            elif end == n-1 or end < n-1 and s[end+1] == " ":
                self.Reversed(s, start, end)
                end += 1
                start = end
            else:
                end += 1
        return ''.join(s)


if __name__ == '__main__':
    string = 'I am a student.'
    s = Solution()
    print(s.ReverseSentence(string))