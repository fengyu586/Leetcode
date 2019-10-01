# -*- coding: utf-8 -*-
# @Author  : Jing
# @FileName: 17.打印从1到最大的n位数.py
# @IDE: PyCharm
# Solution 1: Iteration
# Solution 2: Recursion


def str_add(string):
    overflow = False
    m = len(string)
    take_over = 0
    for i in range(m-1, -1, -1):
        n_sum = int(string[i])
        if i == n-1:
            n_sum +=  1
        else:
            n_sum += take_over
        if n_sum >= 10:
            if i == 0:
                overflow = True
            n_sum -= 10
            take_over = 1
            string[i] = str(n_sum)
        else:
            string[i] = str(n_sum)
            break
    return overflow


def print_digit(string):
    is_being0 = True
    m = len(string)
    for i in range(m):
        if is_being0 and string[i] != '0':
            is_being0 = False
        if not is_being0:
            print(''.join(string[i:]))
            break


def print_max_of_n_digit1(m):
    if m <= 0:
        return None
    string = ['0' for _ in range(m)]
    while not str_add(string):
        print_digit(string)
    del string


def get_string_recursively(string, length, index):
    if index == length - 1:
        if string == ['0'] * length:
            return None
        else:
            print_digit(string)
            return None
    for i in range(10):
        string[index+1] = str(i)
        get_string_recursively(string, length, index+1)


def print_max_of_n_digit2(m):
    if m <= 0:
        return None
    string = ['0' for _ in range(m)]
    get_string_recursively(string, m, -1)
    del string


if __name__ == '__main__':
    n = 2
    print_max_of_n_digit2(n)





