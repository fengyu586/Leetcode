# -*- coding: utf-8 -*-
# @Author  : Jing
# @FileName: 89. Gray Code.py
# @IDE: PyCharm
# https://leetcode.com/problems/gray-code/
# Solution 1: DP    O(2^n)Time O(2^n)Space
# Solution 2: formula   save the highest position,
# then current xor better higher .  O(2^n)Time O(2^n)Space


class Solution:
    def grayCode1(self, n):
        if n < 0:
            return []
        res, add = [0], 1
        for i in range(n):
            m = len(res)
            for j in range(m-1, -1, -1):
                res.append(res[j]+add)
            add = add << 1
        return res

    def grayCode2(self, n):
        return [i^i>>1 for i in range(2**n)]


if __name__ == '__main__':
    n = 3
    s = Solution()
    print(s.grayCode2(n))


