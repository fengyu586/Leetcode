# -*- coding: utf-8 -*-
# @Author  : Jing
# @FileName: 43.1~n整数中1出现的次数.py
# @IDE: PyCharm
# Solution 1: 暴力解 O(nlogn)Time O(1)Space logn 为n的位数
# Solution 2: 诸位求解 O(logn)Time O(n)Space


class Solution:
    def NumberOf1Between1AndN_Solution1(self, n):
        # write code here
        res = 0
        for i in range(1, n+1):
            tmp_n = str(i)
            for j in tmp_n:
                if j == '1':
                    res += 1
        return res

    def numberOf1(self, n):
        length = len(n)
        first = int(n[0])
        if length == 1:
            if first == 0:
                return 0
            else:
                return 1
        # 求最高位为1的数字个数
        num_first_digit = 0
        if first == 1:
            num_first_digit = int(n[1:]) + 1
        elif first > 1:
            num_first_digit = 10 ** (length - 1)
        # 求次高位为1的数字个数
        num_other_digit = first * (length - 1) * 10 ** (length - 2)
        # 求去掉最高位后的数字中1的个数
        num_recursion_digit = self.numberOf1(n[1:])
        return num_first_digit + num_other_digit + num_recursion_digit

    def NumberOf1Between1AndN_Solution2(self, n):
        # write code here
        if n <= 0:
            return 0
        return self.numberOf1(str(n))


if __name__ == '__main__':
    n = 21345
    s = Solution()
    print(s.NumberOf1Between1AndN_Solution2(n))