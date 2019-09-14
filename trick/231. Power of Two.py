# -*- coding: utf-8 -*-
# @Author  : Jing
# @FileName: 231. Power of Two.py
# @IDE: PyCharm
# https://leetcode.com/problems/power-of-two/
# Solution 1: Recursion O(1)Time O(log n)Space
# Solution 2: Iteration O(log n)Time O(1)Space
# Solution 3: O(1)Time O(1)Space
# Solution 4: O(1)Time O(1)Space

class Solution:
    def isPowerOfTwo(self, n):
        if n == 1:
            return True
        if n%2 != 0 or n == 0:
            return False
        else:
            return self.isPowerOfTwo(n//2)

    def isPowerOfTwo1(self, n):
        if n == 0:
            return False
        if n == 1:
            return True
        while n % 2 == 0:
            n //= 2
            if n == 1:
                return True
        return False

    def isPowerOfTwo2(self, n):
        return  n and n & (-n) == n

    def isPowerOfTwo3(self, n):
        return bin(n).count('1') == 1


if __name__ == '__main__':
    s = Solution()
    n = 0
    print(s.isPowerOfTwo3(n))



