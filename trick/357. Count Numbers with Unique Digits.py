# -*- coding: utf-8 -*-
# @Author  : Jing
# @FileName: 357. Count Numbers with Unique Digits.py
# @IDE: PyCharm
# https://leetcode.com/problems/count-numbers-with-unique-digits/


class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n < 0:
            return 0
        if n == 0:
            return 1
        res, tmp = 10, 9
        for i in range(1, min(10, n)):
            tmp *= 10-i
            res += tmp
        return res


if __name__ == '__main__':
    n = 2
    s = Solution()
    print(s.countNumbersWithUniqueDigits(n))
