# -*- coding: utf-8 -*-
# @Author  : Jing
# @FileName: 79. Word Search.py
# @IDE: PyCharm
# https://leetcode.com/problems/word-search/
# Solution: backtrace


class Solution:
    def helper(self, board, word, rows, cols, row, col, seen, index):
        if index == len(word):
            return True
        is_exist = False
        if 0 <= row < rows and 0 <= col < cols and not seen[row][col] and board[row][col]==word[index]:
            seen[row][col] = True
            index += 1
            is_exist = self.helper(board, word, rows, cols, row-1, col, seen, index) or self.helper(board, word, rows, cols, row+1, col, seen, index) or self.helper(board, word, rows, cols, row, col-1, seen, index) or self.helper(board, word, rows, cols, row, col+1, seen, index)
            if not is_exist:
                seen[row][col] = False
                index -= 1
        return is_exist

    def exist(self, board, word):
        if not board or not board[0] or not word:
            return False
        rows, cols = len(board), len(board[0])
        seen = [[False for _ in range(cols)] for i in range(rows)]
        index = 0
        for i in range(rows):
            for j in range(cols):
                if self.helper(board, word, rows, cols, i, j, seen, index):
                    return True
        del seen
        return False


if __name__ == '__main__':
    board = [['A', 'B', 'C', 'E'],
             ['S', 'F', 'C', 'S'],
             ['A','D', 'E', 'E']]
    word = 'SEE'
    s = Solution()
    print(s.exist(board, word))

