# -*- coding: utf-8 -*-
# @Author  : Jing
# @FileName: 73. Set Matrix Zeroes.py
# @IDE: PyCharm
# https://leetcode.com/problems/set-matrix-zeroes/
# Solution 1: O(MN)Time O(M+N)Space
# Solution 2: O(MN)Time O(1)Space
# Solution 3: O(MN)Time O(1)Space


class Solution:
    def setZeroes1(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix or not matrix[0]:
            return matrix
        rows, cols = len(matrix), len(matrix[0])
        row, col = [], []
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    row.append(i)
                    col.append(j)
        for i in row:
            for j in range(cols):
                matrix[i][j] = 0
        for i in col:
            for j in range(rows):
                matrix[j][i] = 0
        return matrix

    def setZeroes2(self, matrix):
        if not matrix or not matrix[0]:
            return matrix
        rows, cols = len(matrix), len(matrix[0])
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    matrix[i][j] = float("inf")
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == float("inf"):
                    for k in range(rows):
                        matrix[k][j] = 0
                    for k in range(cols):
                        matrix[i][k] = 0
        return matrix

    def setZeroes(self, matrix):
        if not matrix or not matrix[0]:
            return matrix
        rows, cols = len(matrix), len(matrix[0])
        is_col = False
        for i in range(rows):
            if matrix[i][0] == 0:
                is_col = True
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        if matrix[0][0] == 0:
            for i in range(1, cols):
                matrix[0][i] = 0
        if is_col:
            for i in range(rows):
                matrix[i][0] = 0
        return matrix


if __name__ == '__main__':
    matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    s = Solution()
    print(s.setZeroes(matrix))
