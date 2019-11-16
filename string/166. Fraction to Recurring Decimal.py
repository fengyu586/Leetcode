# -*- coding: utf-8 -*-
# @Author  : Jing
# @FileName: 166. Fraction to Recurring Decimal.py
# @IDE: PyCharm
# https://leetcode.com/problems/fraction-to-recurring-decimal/


class Solution:
    def helper(self, numerator, denominator):
        dic = {}
        s = []
        while numerator != 0 and numerator < denominator and numerator not in dic:
            dic[numerator] = 1
            numerator *= 10
            while numerator not in dic and numerator < denominator:
                dic[numerator] = 1
                numerator *= 10
                s.append('0')
            s.append(str(numerator // denominator))
            numerator %= denominator
        if numerator != 0:
            index = 0
            for i in dic.keys():
                if i != numerator:
                    index += 1
                else:
                    break
            return ''.join(s[:index])+'('+''.join(s[index:]) + ')'
        else:
            return ''.join(s)

    def fractionToDecimal(self, numerator, denominator):
        if denominator == 0:
            return ""
        flag = 1
        if numerator * denominator < 0:
            flag = -1
        numerator, denominator = abs(numerator), abs(denominator)
        res1 = int(numerator / denominator)
        s1 = str(res1)
        if flag == -1:
            s1 = '-' + s1
        num = numerator % denominator
        s2 = self.helper(num, denominator)
        if not s2:
            return s1
        else:
            return s1 + '.' + s2


if __name__ == '__main__':
    num1, num2 = 1, 214748364
    print(num1/num2)
    S = Solution()
    print(S.fractionToDecimal(num1, num2))
