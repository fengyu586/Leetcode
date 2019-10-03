# -*- coding: utf-8 -*-
# @Author  : Jing
# @FileName: 顺时针打印矩阵.py
# @IDE: PyCharm


class Solution:
    # matrix类型为二维列表，需要返回列表
    def startPrintMatrix(self, matrix, rows, cols, start, res):
        end_X = cols - start - 1
        end_Y = rows - start - 1
        # 从左向右打印
        for i in range(start, end_X + 1):
            res.append(matrix[start][i])
        # 从上向下打印
        if start < end_Y:
            for i in range(start + 1, end_Y + 1):
                res.append(matrix[i][end_X])
        # 从右向左打印
        if start < end_X and start < end_Y:
            for i in range(end_X - 1, start - 1, -1):
                res.append(matrix[end_Y][i])
        # 从下向上打印
        if start < end_Y - 1 and start < end_X:
            for i in range(end_Y - 1, start, -1):
                res.append(matrix[i][start])

    def printMatrix(self, matrix):
        # write code here
        if not matrix:
            return None
        if len(matrix) == 0 and len(matrix[0]) == 0:
            return None
        res = []
        rows, cols = len(matrix), len(matrix[0])
        if rows == 0 or cols == 0:
            return None
        start = 0
        while rows > 2 * start and len(matrix[0]) > 2 * start:
            self.startPrintMatrix(matrix, rows, cols, start, res)
            start += 1
        return res


if __name__ == '__main__':
    nums = [[1],[2],[3],[4],[5]]
    s = Solution()
    print(s.printMatrix(nums))