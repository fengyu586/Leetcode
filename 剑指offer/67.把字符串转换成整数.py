# -*- coding: utf-8 -*-
# @Author  : Jing
# @FileName: 67.把字符串转换成整数.py
# @IDE: PyCharm
# https://leetcode.com/problems/string-to-integer-atoi/


class Solution:
    def myAtoi1(self, str: str) -> int:
        if not str:
            return 0
        max_val, min_val = 1 << 32 - 1, - 1 << 31
        i, n = 0, len(str)
        while i < n and str[i].isspace():
            i += 1
        if i >= n or (str[i] != '+' and str[i] != '-' and not str[i].isdigit()):
            return 0
        flag = 1
        if str[i] == '-':
            flag = -1
            i += 1
        elif str[i] == '+':
            i += 1
        s = []
        while i < n:
            if str[i].isdigit():
                s.append(str[i])
                i += 1
            else:
                break
        s = ''.join(s)
        if not s:
            return 0
        num = flag*int(s)
        if flag > 0 and num > max_val:
            return max_val
        elif flag < 0 and num < min_val:
            return min_val
        else:
            return num

    def myAtoi2(self, str: str) -> int:
        if not str:
            return 0
        max_val, min_val = (1<<31) - 1, -(1<<31)
        i, n = 0, len(str)
        while i < n and str[i].isspace():
            i += 1
        if i >= n or (str[i] != '+' and str[i] != '-' and not str[i].isdigit()):
            return 0
        flag = 1
        if str[i] == '-':
            flag = -1
            i += 1
        elif str[i] == '+':
            i += 1
        s = []
        while i < n:
            if str[i].isdigit():
                s.append(str[i])
                i += 1
            else:
                break
        s = ''.join(s)
        if not s:
            return 0
        num = flag*int(s)
        if flag > 0 and num > max_val:
            return max_val
        elif flag < 0 and num < min_val:
            return min_val
        else:
            return num


if __name__ == '__main__':
    string = '42'
    s = Solution()
    print(s.myAtoi2(string))

