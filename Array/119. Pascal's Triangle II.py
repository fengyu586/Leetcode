# -*- coding: utf-8 -*-
# @Author  : Jing
# @FileName: 119. Pascal's Triangle II.py
# @IDE: PyCharm
# https://leetcode.com/problems/pascals-triangle-ii/


class Solution:
    def getRow(self, rowIndex):
        res = []
        for i in range(0, rowIndex+1):
            res = [1]+res
            if i > 1:
                for j in range(1, i):
                    res[j] += res[j+1]
        return res

    def getRow1(self, rowIndex):
        res = [1]
        if rowIndex == 0:
            return res
        res += [1]
        if rowIndex == 1:
            return res
        for i in range(2, rowIndex+1):
            res = [res[0]]+[res[j]+res[j+1] for j in range(i-1)]+[res[-1]]
        return res

    def getRow2(self, rowIndex):
        res = [1]
        for i in range(1, rowIndex+1):
            pre = [0]+res+[0]
            res = [pre[j]+pre[j+1] for j in range(i+1)]
        return res


if __name__ == '__main__':
    rowIndex = 3
    s = Solution()
    print(s.getRow(rowIndex))       # Output is [1,3,3,1].


