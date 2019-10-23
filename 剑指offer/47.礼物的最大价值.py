# -*- coding: utf-8 -*-
# @Author  : Jing
# @FileName: 47.礼物的最大价值.py
# @IDE: PyCharm
# Solution 1: O(mn)Time, O(mn)Space
# Solution 2: O(mn)Time, O(n)Space


class Solution:
    def getMaxValue1(self, values):
        if not values:
            return 0
        rows, cols = len(values), len(values[0])
        dp = [[0 for _ in range(cols)] for i in range(rows)]
        dp[0][0] = values[0][0]
        for col in range(1, cols):
            dp[0][col] = dp[0][col-1]+values[0][col]
        for row in range(1, rows):
            dp[row][0] = dp[row-1][0]+values[row][0]
        for row in range(1, rows):
            for col in range(1, cols):
                dp[row][col] = max(dp[row-1][col], dp[row][col-1])+values[row][col]
        return dp[-1][-1]

    def getMaxValue2(self, values):
        if not values:
            return 0
        rows, cols = len(values), len(values[0])
        dp = [[0 for _ in range(cols)] for i in range(2)]
        dp[0][0] = values[0][0]
        for col in range(1, cols):
            dp[0][col] = dp[0][col-1]+values[0][col]
        for row in range(1, rows):
            row_index = row % 2
            for col in range(0, cols):
                if col == 0:
                    dp[row_index][col] = dp[1-row_index][col]+values[row][col]
                else:
                    dp[row_index][col] = max(dp[1-row_index][col], dp[row_index][col-1])+values[row][col]
        return dp[1-rows%2][-1]


if __name__ == '__main__':
    values = [[1, 10, 3, 8], [12, 2, 9, 6], [5, 7, 4, 11], [3, 7, 16, 5]]
    s = Solution()
    print(s.getMaxValue2(values))
