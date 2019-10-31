# -*- coding: utf-8 -*-
# @Author  : Jing
# @FileName: 77. Combinations.py
# @IDE: PyCharm
# https://leetcode.com/problems/combinations/
# Solution 1: recursively


class Solution:
    def __init__(self):
        self.res = []

    def helper(self, k, i, n, cur):
        if len(cur) == k:
            self.res.append(cur)
            return
        else:
            for j in range(i, n + 1):
                self.helper(k, j + 1, n, cur + [j])

    def combine(self, n, k):
        if n < 1 or k > n:
            return []
        self.helper(k, 1, n, [])
        return self.res


if __name__ == '__main__':
    n, k = 4, 3
    s = Solution()
    print(s.combine(n, k))
