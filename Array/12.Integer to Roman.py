# -*- coding: utf-8 -*-
# @Author  : Jing
# @FileName: 12.Integer to Roman.py
# @IDE: PyCharm
# https://leetcode.com/problems/integer-to-roman/


class Solution:
    def get_str(self, num, dic):
        if num == 0:
            return ''
        n = len(str(num))-1
        number = 10**n
        first_number = int(str(num)[0])
        if first_number == 4:
            return dic[number]+dic[5*number]
        elif first_number == 9:
            return dic[number]+dic[10*number]
        elif first_number < 4:
            return dic[number]*first_number
        else:
            return dic[5*number]+dic[number]*(first_number-5)


    def inToRoman(self, num):
        num = str(num)
        n = len(num)
        res = ''
        dic = {1:'I', 5:'V', 10:'X', 50:'L', 100:'C', 500:'D', 1000:'M'}
        for i in range(n):
            res += self.get_str(int(num[i])*10**(n-1-i), dic)
        return res

if __name__ == '__main__':
    num = 1995
    s = Solution()
    print(s.inToRoman(num))