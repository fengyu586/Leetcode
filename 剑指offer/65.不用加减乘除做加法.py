# -*- coding: utf-8 -*-
# @Author  : Jing
# @FileName: 65.不用加减乘除做加法.py
# @IDE: PyCharm


class Solution:
    def Add(self, num1, num2):
        # write code here
        while num2 != 0:
            num1, num2 = (num1^num2)&0xFFFFFFFF, (num1&num2)<<1
        return num1 if num1 >> 31 == 0 else num1 - (2 << 31)

    def Add2(self, num1, num2):
        return num1+num2

if __name__ == '__main__':
    num1 = 1
    num2 = -2
    s = Solution()
    print(s.Add(num1, num2))
    print(s.Add2(num1, num2))
