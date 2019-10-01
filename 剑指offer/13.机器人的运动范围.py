# -*- coding: utf-8 -*-
# @Author  : Jing
# @FileName: 13.机器人的运动范围.py
# @IDE: PyCharm


def get_digit_sum(num):
    count = 0
    while num > 0:
        count += num % 10
        num //= 10
    return count


def check(rows, cols, row, col, threshold, visited):
    if col >= 0 and col < cols and row >= 0 and row < rows and get_digit_sum(
            row) + get_digit_sum(col) <= threshold and not visited[row][col]:
        return True
    return False


def moving_count_core(threshold, rows, cols, row, col, visited):
    count = 0
    if check(rows, cols, row, col, threshold, visited):
        visited[row][col] = True
        count = 1 + moving_count_core(threshold, rows, cols, row-1, col, visited)
        count += moving_count_core(threshold, rows, cols, row, col-1, visited)
        count += moving_count_core(threshold, rows, cols, row+1, col, visited)
        count += moving_count_core(threshold, rows, cols, row, col+1, visited)
    return count


def moving_count(threshold, rows, cols):
    if threshold < 0 or rows <= 0 or cols <= 0:
        return 0
    if rows < 1 and cols < 1 or threshold == 0:
        return 1
    visited = [[False for _ in range(cols)] for i in range(rows)]
    count = moving_count_core(threshold, rows, cols, 0, 0, visited)
    del visited
    return count


if __name__ == '__main__':
    rows, cols = 5, 4
    threshold = 5
    print(moving_count(threshold, rows, cols))


