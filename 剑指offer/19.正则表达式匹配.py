# -*- coding: utf-8 -*-
# @Author  : Jing
# @FileName: 19.正则表达式匹配.py
# @IDE: PyCharm


def match(str, pattern):
    if str is None or pattern is None:
        return False
    return match_core(str, pattern)


def match_core(str, pattern):
    if len(str) == 0 and len(pattern) == 0:
        return True
    if len(str) > 0 and len(pattern) == 0:
        return False
    if len(pattern) > 1 and pattern[1] == '*':
        if str and (str[0] == pattern[0] or pattern[0] == '.'):
            return match_core(str, pattern[2:]) or match_core(str[1:], pattern[2:]) or match_core(str[1:], pattern)
        else:
            return match_core(str, pattern[2:])
    if str and (str[0] == pattern[0] or pattern[0] == '.'):
        return match_core(str[1:], pattern[1:])
    return False


if __name__ == '__main__':
    str1 = ""
    str2 = ""
    print(match(str1, str2))