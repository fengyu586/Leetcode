# -*- coding: utf-8 -*-
# @Author  : Jing
# @FileName: 16.数值的整数次方.py
# @IDE: PyCharm


invalid_input = False
def power1(base, exponent):
    invalid_input = False
    # 注意0不能为除数
    if base == 0:
        if exponent < 0:
            invalid_input = True
        else:
            pass
        return 0
    if base == 1:
        return 1
    abs_exponent = -exponent if exponent < 0 else exponent
    res = 1
    for time in range(abs_exponent):
        res *= base
    if exponent < 0:
        return 1/res
    else:
        return res


def power2(base, exponent):
    invalid_input = False
    if base == 0 and exponent < 0:
        invalid_input = True
        return 0
    abs_exponent = -exponent if exponent < 0 else exponent
    if abs_exponent == 0:
        return 1
    if abs_exponent == 1:
        return base
    res = power2(base, exponent >> 1)
    res *= res
    if exponent & 0x1 == 1:
        res *= base
    if exponent < 0:
        return 1/res
    else:
        return res



if __name__ == '__main__':
    base = 0
    exponent = -5
    print(power2(base, exponent))





