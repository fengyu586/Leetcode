# -*- coding: utf-8 -*-
# @Author  : Jing
# @FileName: 矩阵中的路径.py
# @IDE: PyCharm
# Solution 1: DFS（回溯法）


class Solution:
    def hasPath(self, matrix, rows, cols, path):
        if len(matrix) == 0:
            return False
        if len(path) == 0:
            return True
        # parse matrix
        m = []
        for i in range(rows):
            offset = i * cols
            row = []
            for j in range(cols):
                row.append(matrix[offset + j])
            m.append(row)

        # build visited
        visited = [[False for j in range(cols)] for i in range(rows)]

        # scan all cells
        for i in range(rows):
            for j in range(cols):
                if self.dfs(m, visited, i, j, rows, cols, path):
                    return True
        return False

    def dfs(self, m, visited, i, j, rows, cols, path):
        # terminal conditions
        if i < 0 or i == rows:
            return False
        if j < 0 or j == cols:
            return False
        if visited[i][j]:
            return False

        # visit self
        if path[0] != m[i][j]:
            return False
        visited[i][j] = True
        nextPath = path[1:]
        if len(nextPath) == 0:
            return True

        # visit neighbours
        if self.dfs(m, visited, i + 1, j, rows, cols, nextPath):
            return True
        if self.dfs(m, visited, i - 1, j, rows, cols, nextPath):
            return True
        if self.dfs(m, visited, i, j + 1, rows, cols, nextPath):
            return True
        if self.dfs(m, visited, i, j - 1, rows, cols, nextPath):
            return True

        # unvisit self
        visited[i][j] = False
        return False


if __name__ == '__main__':
    nums = ['A', 'B', 'C', 'E', 'S', 'F', 'C', 'S', 'A', 'D', 'E', 'E']
    rows, cols = 3, 4
    path = ['A', 'B', 'C', 'C', 'E', 'D']
    s = Solution()
    print(s.hasPath(nums, rows, cols, path))

