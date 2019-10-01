# -*- coding: utf-8 -*-
# @Author  : Jing
# @FileName: 矩阵中的路径.py
# @IDE: PyCharm


def has_path_core(matrix, rows, cols, row, col, string, path_length, visited):
    if path_length == len(string):
        return True
    hasPath = False
    if 0 <= col < cols and 0 <= row < rows and matrix[
            row][col] == string[path_length] and not visited[row][col]:
        path_length += 1
        visited[row][col] = True
        hasPath = has_path_core(
            matrix,
            rows,
            cols,
            row -
            1,
            col,
            string,
            path_length,
            visited) or has_path_core(
            matrix,
            rows,
            cols,
            row,
            col -
            1,
            string,
            path_length,
            visited) or has_path_core(
            matrix,
            rows,
            cols,
            row +
            1,
            col,
            string,
            path_length,
            visited) or has_path_core(
                matrix,
                rows,
                cols,
                row,
                col +
                1,
                string,
                path_length,
            visited)
    if not hasPath:
        path_length -= 1
        visited[row][col] = False
    return hasPath


def has_path(matrix, rows, cols, string):
    if not matrix or rows < 1 or cols < 1 or not string:
        return False
    path_length = 0
    visited = [[False for _ in range(cols)] for i in range(rows)]
    for row in range(rows):
        for col in range(cols):
            if has_path_core(matrix, rows, cols, row, col, string, path_length, visited):
                return True
    del visited
    return False


if __name__ == '__main__':
    matrix = [['a', 'b', 't', 'g'], ['c', 'f', 'c', 's'], ['j', 'd', 'e', 'h']]
    rows, cols = len(matrix), len(matrix[0])
    string = 'agsc'
    print(has_path(matrix, rows, cols, string))

