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
        if i == m-1:
            n_sum += 1
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


def add_str1(nums0, nums1, flag):
    m, n = len(nums0), len(nums1)
    nums1 = ['0' for _ in range(m-n)]+nums1
    take_over = 0
    if not flag:
        # 相减
        for i in range(m-1, -1, -1):
            if i == -1:
                diff = int(nums0[i])-int(nums1[i])
            else:
                diff = int(nums0[i])-int(nums1[i])-take_over
            if diff < 0:
                take_over = 1
                nums0[i] = str(diff+10)
            else:
                nums0[i] = str(diff)
                take_over = 0
    else:
        for i in range(m-1, -1, -1):
            if i == -1:
                diff = int(nums0[i])+int(nums1[i])
            else:
                diff = int(nums0[i])+int(nums1[i])+take_over
            if diff > 10:
                take_over = 1
                nums0[i] = str(diff-10)
            else:
                nums0[i] = str(diff)
                take_over = 0
    for i in range(m):
        if nums0[i] != '0':
            return nums0[i:]
    return '0'


def str_add1(nums0, nums1):
    nums0 = [s for s in str(nums0)]
    nums1 = [s for s in str(nums1)]
    flag0, flag1 = 1, 1
    if nums0[0] == '-':
        flag0 = -1
        nums0 = nums0[1:]
    if nums1[0] == '-':
        flag1 = -1
        nums1 = nums1[1:]
    m, n = len(nums0), len(nums1)
    if m < n:
        nums0, nums1 = nums1, nums0
        flag0, flag1 = flag1, flag0
    elif m == n:
        for i in range(n):
            if nums0[i] < nums1[i]:
                nums0, nums1 = nums1, nums0
                flag0, flag1 = flag1, flag0
                break
    if flag0 == flag1:
        flag = 1
    else:
        flag = 0
    res = add_str1(nums0, nums1, flag)
    if flag0 == -1:
        res = ['-']+res
    print(''.join(res))


if __name__ == '__main__':
    # n = 2
    str0 = 0
    str1 = -0
    str_add1(str0, str1)
    # print_max_of_n_digit2(n)
