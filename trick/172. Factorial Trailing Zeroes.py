# -*- coding: utf-8 -*-
# @Author  : Jing
# @FileName: 172. Factorial Trailing Zeroes.py
# @IDE: PyCharm
# https://leetcode.com/problems/factorial-trailing-zeroes/
# 相当于求n之前的数可以拆出多少个5
# Solution 1: iteration O(log5 n)Time
# Solution 2: recursion O(log5 n)Time

class Solution:
    def trailingZeroes1(self, n):
        res = 0
        while n > 0:
            n //= 5
            res += n
        return res

    def trailingZeroes2(self, n):
        if n == 0:
            return 0
        else:
            return n//5 + self.trailingZeroes2(n//5)


if __name__ == '__main__':
    s = Solution()
    print(s.trailingZeroes2(25))         # Output is 6

