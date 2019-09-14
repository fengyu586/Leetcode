# -*- coding: utf-8 -*-
# @Author  : Jing
# @FileName: 6. ZigZag Conversion.py
# @IDE: PyCharm
# https://leetcode.com/problems/zigzag-conversion/


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        li = [[] for _ in range(numRows)]
        flag = 0
        i = 0
        idx = 0
        if numRows == 1:
            return s
        while i < len(s):
            li[idx].append(s[i])
            if idx == numRows-1:
                flag = 1
            if idx == 0:
                flag = 0
            if flag:
                idx -= 1
            else:
                idx += 1
            i += 1
        return ''.join([''.join(i) for i in li])

    def convert1(self, s, numRows):
        if numRows == 1:
            return s
        res = ['' for _ in range(numRows)]
        idx = 0
        flag = -1
        for string in s:
            res[idx] += string
            if idx == numRows - 1 or idx == 0:
                flag *= -1
            idx += flag
        return ''.join(res)


if __name__ == '__main__':
    S = Solution()
    s, numRows = "PAYPALISHIRING", 3
    print(S.convert1(s, numRows))          # Output is "PAHNAPLSIIGYIR".

