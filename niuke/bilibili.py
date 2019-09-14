# -*- coding: utf-8 -*-
# @Author  : Jing
# @FileName: bilibili.py
# @IDE: PyCharm
##################### 比较两个版本字符串 #################


def first():
    [v1, v2] = [s.split('.') for s in input().split()]
    if v1 == v2:
        return 0
    n = min(len(v1), len(v2))
    for i in range(n):
        if int(v1[i]) > int(v2[i]):
            return 1
        if int(v1[i]) < int(v2[i]):
            return -1
    if len(v1) > len(v2):
        return 1
    if len(v1) < len(v2):
        return -1

def second():
    n = int(input())
    li = []
    for i in range(n):
        cur = list(map(int, input().split(',')))
        li.append(cur)
    dp = [[0 for i in range(n)] for _ in range(n)]
    dp[0][0] = li[0][0]
    for i in range(1, n):
        dp[i][0] = dp[i-1][0]+li[i][0]
    for i in range(1, n):
        dp[0][i] =  dp[0][i-1]+li[0][i]
    for i in range(1, n):
        for j in range(1, n):
            dp[i][j] = min(dp[i][j-1], dp[i-1][j])+li[i][j]
    return dp[-1][-1]


def third():
    [m, n] = list(map(int, input().split()))
    matrix = []
    for i in range(m):
        li = list(map(int, input().split()))
        matrix.append(li)
    li = []
    i, j = 0, 0
    # top
    while j < n:
        li.append(matrix[i][j])
        j += 1
    n -= 1
    # right
    while i < m:
        li.append(matrix[i][j-1])
        i += 1
    m -= 1
    # bottom

def main():
    # first()
    # print(second())
    third()


if __name__ == '__main__':
    main()







