# -*- coding: utf-8 -*-
# @Author  : Jing
# @FileName: 58.1左旋转字符串.py
# @IDE: PyCharm


class Solution:
    def LeftRotateString1(self, s, n):
        # write code here
        if not s:
            return s
        length = len(s)
        s = list(s)
        res = [i for i in s]
        n = n % length
        for i in range(length):
            res[i - n] = s[i]
        return ''.join(res)

    def Reversed(self, s, start, end):
        if not s:
            return
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1
        return

    def LeftRotateString2(self, s, n):
        if not s:
            return s
        s = list(s)
        length = len(s)
        n %= length
        self.Reversed(s, 0, n-1)
        self.Reversed(s, n, length-1)
        self.Reversed(s, 0, length-1)
        return ''.join(s)


if __name__ == '__main__':
    string = 'abcXYZdef'
    k = 3
    s = Solution()
    print(s.LeftRotateString2(string, k))


