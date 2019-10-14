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

    def NumberOf1Between1AndN_Solution2(self, n):
        str_n = str(n)
        length = len(str_n)
        if length == 1:
            if n == 0:
                return 0
            else:
                return 1
        first = int(str_n[0])

        # 满足最高位为1的数字的个数，仅关心最高位为1
        num_first_1 = 0
        if first > 1:
            num_first_1 = 10**(length-1)
        elif first == 1:
            num_first_1 = int(str_n[1:])+1

        # 求满足最高位非零，其他位任意一位为1的数字个数，仅关心其他位为1，最高位是否为1不关心。
        num_other_1 = first*(length-1)*10**(length-2)
        num_recursion_1 = self.NumberOf1Between1AndN_Solution2(int(str_n[1:]))
        return num_first_1+num_other_1+num_recursion_1


if __name__ == '__main__':
    n = 21345
    s = Solution()
    print(s.NumberOf1Between1AndN_Solution2(n))