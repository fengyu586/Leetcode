# -*- coding: utf-8 -*-
# @Author  : Jing
# @FileName: 15.二进制中1的个数.py
# @IDE: PyCharm


def number_of_10(n):
    count = 0
    flag = 1
    n = n & 0xffffffff
    while n:
        if n & flag:
            count += 1
        n = n >> 1
    return count


def number_of_11(n):
    count = 0
    # 先将n转换为补码，
    # 若n为负数，则计算其补码中1的个数，
    # 若n为非负数，则其补码仍为其本身
    n = n & 0xffffffff      # 先将n转换为补码
    while n:
        count += 1
        # n-1和n相与相当于消除了n中最右边的一个1
        n = (n-1) & n
    return count


if __name__ == '__main__':
    n = 1
    print(number_of_10(n))
