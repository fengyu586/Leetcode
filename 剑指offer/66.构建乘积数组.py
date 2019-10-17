# -*- coding: utf-8 -*-
# @Author  : Jing
# @FileName: 66.构建乘积数组.py
# @IDE: PyCharm
# Solution 1: 暴力法 O(n^2)Time O(n)Space
# Solution 2: 记忆化数组 O(n)Time O(n)Space


class Solution:
    def sub_multiply(self, A, start, end):
        res = 1
        for i in range(start, end + 1):
            res *= A[i]
        return res

    def multiply1(self, A):
        # write code here
        if not A:
            return A
        n = len(A)
        B = list(range(n))
        for i in range(n):
            B[i] = self.sub_multiply(A, 0, i - 1) * \
                self.sub_multiply(A, i + 1, n - 1)
        return B

    def multiply2(self, A):
        if not A:
            return A
        n = len(A)
        C, D = list(range(n)), list(range(n))
        C[0], D[n - 1] = 1, 1
        for i in range(1, n):
            C[i] = C[i - 1] * A[i - 1]
            D[n - 1 - i] = D[n - i] * A[n - i]
        for i in range(n):
            C[i] *= D[i]
        return C


if __name__ == '__main__':
    nums = list(range(1, 11))
    s = Solution()
    print(s.multiply2(nums))
