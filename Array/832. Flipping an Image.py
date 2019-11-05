# -*- coding: utf-8 -*-
# @Author  : Jing
# @FileName: 832. Flipping an Image.py
# @IDE: PyCharm
# https://leetcode.com/problems/flipping-an-image/
# Solution 1: O(mn)Time, O(1)Space


class Solution:
    def rowInvert(self, A, row):
        cols = len(A[row])
        l, r = 0, cols - 1
        while l <= r:
            A[row][l], A[row][r] = 1-A[row][r], 1-A[row][l]
            l += 1
            r -= 1
        return

    def flipAndInvertImage(self, A):
        if not A:
            return A
        rows = len(A)
        for row in range(rows):
            self.rowInvert(A, row)
        return A


if __name__ == '__main__':
    nums = [[1, 1, 0], [1, 0, 1], [0, 0, 0]]
    s = Solution()
    print(s.flipAndInvertImage(nums))
