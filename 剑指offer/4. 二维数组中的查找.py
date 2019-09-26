# -*- coding: utf-8 -*-
# @Author  : Jing
# @FileName: 4. 二维数组中的查找.py
# @IDE: PyCharm
###################################
# 题目：在一个二维数组中，
# 每一行都按照从左到右递增的顺序排序，
# 每一列都按照从上到下递增的顺序排序。
# 请完成一个函数，
# 输入这样的一个二维数组和一个整数，
# 判断数组中是否含有该整数。
###################################


class Solution:
    def find_target(self, nums, rows, cols, target):
        flag = False
        if nums and rows > 0 and cols > 0:
            row, col = 0, cols-1
            while col >= 0 and row < rows:
                if nums[row][col] > target:
                    col -= 1
                elif nums[row][col] == target:
                    flag = True
                    break
                else:
                    row += 1
        return flag


if __name__ == '__main__':
    nums = [[1, 2, 8, 9],
            [2, 4, 9, 12],
            [4, 7, 10, 13],
            [6, 8, 11, 15]]
    rows, cols = 4, 4
    target = 7
    s = Solution()
    print(s.find_target(nums, rows, cols, target))          #Output is True.
