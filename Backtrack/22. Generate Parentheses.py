# -*- coding: utf-8 -*-
# @Author  : Jing
# @FileName: 22. Generate Parentheses.py
# @IDE: PyCharm
# https://leetcode.com/problems/generate-parentheses/
# Solution 1: Brute Force O((2^2n)*n)Time O((2^2n)*n)Space
# Solution 2: Backtracking O((4^n)/(n^0.5))Time O((4^n)/(n^0.5))Space
# Solution 3: Closure Number O((4^n)/(n^0.5))Time O((4^n)/(n^0.5))Space


class Solution:
    def valid(self, A):
        bal = 0
        for c in A:
            if c == '(':
                bal += 1
            else:
                bal -= 1
            if bal < 0:
                return False
        return bal == 0

    def generate(self, n, res, A ):
        if len(A) == 2*n:
            if self.valid(A):
                res.append(''.join(A))
        else:
            A.append('(')
            self.generate(n, res, A)
            A.pop()
            A.append(')')
            self.generate(n, res, A)
            A.pop()



    def generateParenthesis1(self, n):
        if n <= 0:
            return []
        res = []
        self.generate(n, res, [])
        return res



    def backtracking(self, n, res, s='', left=0, right=0):
        if len(s) == 2 * n:
            res.append(s)
            return
        if left < n:
            self.backtracking(n, res, s + '(', left + 1, right)
        if right < left:
            self.backtracking(n, res, s + ')', left, right + 1)

    def generateParenthesis2(self, n):
        if n <= 0:
            return []
        res = []
        self.backtracking(n, res)
        return res

    def generateParenthesis3(self, n):
        if n == 0:
            return ['']
        res = []
        for c in range(n-1, -1, -1):
            for left in self.generateParenthesis3(c):
                for right in self.generateParenthesis3(n-1-c):
                    res.append('({}){}'.format(left, right))
        return res


if __name__ == '__main__':
    n = 3
    s = Solution()
    print(s.generateParenthesis3(n))

