# -*- coding: utf-8 -*-
# @Author  : Jing
# @FileName: 54. Spiral Matrix.py
# @IDE: PyCharm
# https://leetcode.com/problems/spiral-matrix/
# Solution 1: simulate O(N)Time O(N)Space
# Solution 2: floor by floor O(N)Time O(N)Space


class Solution:
    def spiralOrder1(self, matrix):
        res = []
        if not matrix or not matrix[0]:
            return res
        rows, cols = len(matrix), len(matrix[0])
        seen = [[False for _ in range(cols)] for __ in range(rows)]
        dr, dc = [0, 1, 0, -1], [1, 0, -1, 0]
        row, col, di = 0, 0, 0
        while len(res) < rows*cols:
            res.append(matrix[row][col])
            seen[row][col] = True
            r, c = row+dr[di], col+dc[di]
            if 0 <= r < rows and 0 <= c < cols and not seen[r][c]:
                row, col = r, c
            else:
                di = (di+1) % 4
                row, col = row+dr[di], col+dc[di]
        return res

    def sprial_coords(self, r1, c1, r2, c2):
        for c in range(c1, c2+1):
            yield r1, c
        for r in range(r1+1, r2+1):
            yield r, c2
        if r1 < r2 and c1 < c2:
            for c in range(c2-1, c1, -1):
                yield r2, c
            for r in range(r2, r1, -1):
                yield r, c1


    def spiralOrder(self, matrix):
        res = []
        if not matrix or not matrix[0]:
            return res
        rows, cols = len(matrix), len(matrix[0])
        c1, c2 = 0, cols-1
        r1, r2 = 0, rows-1
        while r1 <= r2 and c1 <= c2:
            for r, c in self.sprial_coords(r1, c1, r2, c2):
                print(r, c)
                res.append(matrix[r][c])
            r1 += 1
            r2 -= 1
            c1 += 1
            c2 -= 1
        return res


if __name__ == '__main__':
    nums = [
            [1, 2, 3],
            [5, 6, 7],
            [19, 20, 21],
            [9, 10, 11]
                        ]
    s = Solution()
    print(s.spiralOrder(nums))




