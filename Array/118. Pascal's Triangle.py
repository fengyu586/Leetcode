# -*- coding: utf-8 -*-
# @Author  : Jing
# @FileName: 118. Pascal's Triangle.py
# @IDE: PyCharm


class Solution:
    def generate(self, numRows):
        if numRows == 0:
            return None
        res = [[1]]
        for i in range(1, numRows):
            cur = [0 for _ in range(i+1)]
            cur[0], cur[-1] = res[-1][0], res[-1][-1]
            l, r = 0, 1
            while r<len(res[-1]):
                cur[r] = res[-1][l]+res[-1][r]
                l += 1
                r += 1
            res.append(cur)
        return res

    def generate1(self, numRows):
        if numRows == 0:
            return None
        res = [[1]]
        for i in range(1, numRows):
            tmp = [0]+res[-1]+[0]
            res.append([tmp[i]+tmp[i+1] for i in range(len(tmp)-1)])
        return res


if __name__ == '__main__':
    s = Solution()
    n = 5
    print(s.generate1(n))      # Output is [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]].
