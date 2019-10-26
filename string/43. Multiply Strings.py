# -*- coding: utf-8 -*-
# @Author  : Jing
# @FileName: 43. Multiply Strings.py
# @IDE: PyCharm


class Solution:
    def multiply(self, num1, num2):
        res = 0
        n, m = len(num1), len(num2)
        for i in range(m):
            for j in range(n):
                res += int(num1[n-1-j]+'0'*j)*int(num2[m-1-i]+'0'*i)
        return str(res)


if __name__ == '__main__':
    num1, num2 = '2', '3'
    s = Solution()
    print(s.multiply(num1, num2))
