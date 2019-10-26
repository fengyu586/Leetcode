# -*- coding: utf-8 -*-
# @Author  : Jing
# @FileName: 36. Valid Sudoku.py
# @IDE: PyCharm
# https://leetcode.com/problems/valid-sudoku/
# Solution 1: Bruce Force O(3^4)Time O(3*3)Space



class Solution:
    def check(self, board, rows, cols, flag, reverse=False, whole=False):
        if not flag:
            return flag
        dic = {}
        for row in range(rows):
            if not whole:
                dic = {}
            for col in range(cols):
                if reverse:
                    num = board[col][row]
                else:
                    num = board[row][col]
                if num not in dic:
                    dic[num] = 1
                elif num != '.':
                    return False
                else:
                    dic[num] += 1
        return True

    def isValidSudoku(self, board):
        if not board:
            return False
        rows, cols = len(board), len(board[0])
        flag = self.check(board, rows, cols, True)
        flag = self.check(board, cols, rows, flag, True)
        for i in range(3):
            row_board = board[i*3:(i+1)*3]
            for j in range(3):
                sub_board = [tmp[j*3:(j+1)*3] for tmp in row_board]
                flag = self.check(sub_board, 3, 3, flag, False, True)
        return flag


if __name__ == '__main__':
    nums = [[".",".",".",".","5",".",".","1","."],
            [".","4",".","3",".",".",".",".","."],
            [".",".",".",".",".","3",".",".","1"],
            ["8",".",".",".",".",".",".","2","."],
            [".",".","2",".","7",".",".",".","."],
            [".","1","5",".",".",".",".",".","."],
            [".",".",".",".",".","2",".",".","."],
            [".","2",".","9",".",".",".",".","."],
            [".",".","4",".",".",".",".",".","."]]
    s = Solution()
    print(s.isValidSudoku(nums))



