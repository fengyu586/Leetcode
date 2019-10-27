# -*- coding: utf-8 -*-
# @Author  : Jing
# @FileName: 48. Rotate Image.py
# @IDE: PyCharm
# https://leetcode.com/problems/rotate-image/
# Solution 1: firstly transpose the whole matrix,
# then reverse every row in the matrix. O(N^2)Time O(1)Space
# Solution 2: firstly save the four element
# which need rotated on the four side,
# then rotate the element in order from outside to inside.
# O(N^2)Time O(1)Space (a temp list with 4 elements)
# Solution 3: the same as Solution 2, but rotate by hand.
# O(N^2)Time O(1)Space


class Solution:
    def transpose(self, matrix):
        rows, cols = len(matrix), len(matrix[0])
        for row in range(rows):
            for col in range(row + 1, rows):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]
        return

    def reverse(self, matrix):
        rows, cols = len(matrix), len(matrix[0])
        for row in range(rows):
            for col in range(cols // 2):
                matrix[row][col], matrix[row][cols-1 - col] = matrix[row][cols-1 - col], matrix[row][col]
        return

    def rotate1(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix or not matrix[0]:
            return matrix
        rows, cols = len(matrix), len(matrix[0])
        if rows != cols:
            return matrix

        # firstly transpose the whole matrix
        self.transpose(matrix)

        # second reverse in every row in the matrix
        self.reverse(matrix)
        return matrix

    def rotate2(self, matrix):
        if not matrix or not matrix[0]:
            return matrix
        rows, cols = len(matrix), len(matrix[0])
        if rows != cols:
            return matrix
        n = rows
        floor_num = n//2

        # tmp = [top， right，bottom，left]
        tmp = [0 for _ in range(4)]
        for i in range(floor_num):
            for j in range(i, n-1-i):
                row, col = i, j
                for k in range(4):
                    tmp[k] = matrix[row][col]
                    row, col = col, n-1-row
                for k in range(4):
                    matrix[row][col] = tmp[(3+k)%4]
                    row, col = col, n-1-row
        return matrix

    def rotate3(self, matrix):
        if not matrix or not matrix[0]:
            return matrix
        rows, cols = len(matrix), len(matrix[0])
        if rows != cols:
            return matrix
        n = rows
        floor_num = n //2
        for i in range(floor_num):
            for j in range(i, n-1-i):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[n-1-j][i]
                matrix[n-1-j][i] = matrix[n-1-i][n-1-j]
                matrix[n-1-i][n-1-j] = matrix[j][n-1-i]
                matrix[j][n-1-i] = tmp
        return matrix





if __name__ == '__main__':
    matrix = [
                [1,2,3],
                [4,5,6],
                [7,8,9]
                        ]
    s = Solution()
    print(s.rotate3(matrix))



