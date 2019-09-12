# -*- coding: utf-8 -*-
# @Author  : Jing
# @FileName: 171. Excel Sheet Column Number.py
# @IDE: PyCharm
# https://leetcode.com/problems/excel-sheet-column-number/


class Solution:
    def titleToNumber(self, s):
        res = 0
        for i in s:
            res *= 26
            res += ord(i)-ord('A')+1
        return res


if __name__ == '__main__':
    S = Solution()
    print(S.titleToNumber('AB'))            # Output is 28




