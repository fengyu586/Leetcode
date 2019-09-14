# -*- coding: utf-8 -*-
# @Author  : Jing
# @FileName: 263. Ugly Number.py
# @IDE: PyCharm
# https://leetcode.com/problems/ugly-number/
# Solution 1: Iteration
# Solution 2: Recursion

class Solution:
    def isUgly(self, num):
        if num == 0:
            return False
        while num != 1:
            if num % 2 == 0:
                num //= 2
            elif num % 3 == 0:
                num //= 3
            elif num % 5 == 0:
                num //= 5
            else:
                return False
        return True

    def isUgly1(self, num):
        if num == 0:
            return False
        if num % 2 == 0:
            num //= 2
        if num % 3 == 0:
            num //= 3
        if num % 5 == 0:
            num //= 5
        if num % 2 == 0 or num % 3 == 0 or num % 5 == 0:
            return self.isUgly1(num)
        elif num == 1:
            return True
        else:
            return False


if __name__ == '__main__':
    num = 16
    s = Solution()
    print(s.isUgly(num))        # Output is True.