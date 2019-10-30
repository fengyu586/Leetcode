# -*- coding: utf-8 -*-
# @Author  : Jing
# @FileName: 59. Spiral Matrix II.py
# @IDE: PyCharm
# https://leetcode.com/problems/spiral-matrix-ii/
# Solution 1: simulate O(N)Time O(N)Space
# Solution 2: floor by floor O(N)Time O(N)Space


class Solution:
    def generateMatrix1(self, n):
        if n < 1:
            return []
        seen = [[False for _ in range(n)] for i in range(n)]
        res = [[0 for _ in range(n)] for i in range(n)]
        dr = [0, 1, 0, -1]
        dc = [1, 0, -1, 0]
        row, col, di = 0, 0, 0
        i = 1
        max_val = n**2
        while i <= max_val:
            res[row][col] = i
            i += 1
            seen[row][col] = True
            r, c = row+dr[di], col+dc[di]
            if 0 <= r < n and 0 <= c < n and not seen[r][c]:
                row, col =r, c
            else:
                di = (di+1)%4
                row += dr[di]
                col += dc[di]
        return res

    def helper(self, r1, c1, r2, c2):
        for c in range(c1, c2 + 1):
            yield r1, c
        for r in range(r1 + 1, r2 + 1):
            yield r, c2
        if r1 < r2 and c1 < c2:
            for c in range(r2 - 1, r1, -1):
                yield r2, c
            for r in range(r2, r1, -1):
                yield r, c1

    def generateMatrix2(self, n):
        if n < 1:
            return []
        max_val = n ** 2
        res = [[0 for _ in range(n)] for i in range(n)]
        r1, r2 = 0, n - 1
        c1, c2 = 0, n - 1
        i = 1
        while i <= max_val:
            for r, c in self.helper(r1, c1, r2, c2):
                res[r][c] = i
                i += 1
            r1 += 1
            r2 -= 1
            c1 += 1
            c2 -= 1
        return res


if __name__ == '__main__':
    n = 3
    s = Solution()
    print(s.generateMatrix1(n))



