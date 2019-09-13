# -*- coding: utf-8 -*-
# @Author  : Jing
# @FileName: 202. Happy Number.py
# @IDE: PyCharm
# https://leetcode.com/problems/happy-number/
# Solution 1: iteration
# Solution 2: recursion


class Solution:
    def isHappy(self, n):
        dic = dict()
        while str(n) not in dic:
            dic[str(n)] = 1
            if n == 1:
                return True
            n = sum([int(i)*int(i) for i in str(n)])
        return False

    def isHappy1(self, n):
        def helper(n ,dic):
            if n == 1:
                return True
            elif str(n) in dic:
                return False
            else:
                dic[str(n)] = 1
                tmp = sum([int(i)*int(i) for i in str(n)])
                return helper(tmp, dic)
        dic = {}
        return helper(n, dic)


if __name__ == '__main__':
    n = 19
    s = Solution()
    print(s.isHappy1(n))



