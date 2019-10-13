# -*- coding: utf-8 -*-
# @Author  : Jing
# @FileName: 38.字符串的排列.py
# @IDE: PyCharm


class Solution:
    def __init__(self):
        self.res = []       # 保存字符串的全排列数组

    def permutation(self, ss, start):
        if start == len(ss):
            string = ''.join(ss)
            self.res.append(string)
            return
        for i in range(start, len(ss)):
            ss[i], ss[start] = ss[start], ss[i]
            self.permutation(ss, start+1)
            ss[i], ss[start] = ss[start], ss[i]     # 还原字符串，防止重复
        return

    def Permutation(self, ss):
        if not ss:
            return ss
        ss = list(ss)
        self.permutation(ss, 0)
        return sorted(self.res)


if __name__ == '__main__':
    s = Solution()
    string = 'abc'
    print(s.Permutation(string))







