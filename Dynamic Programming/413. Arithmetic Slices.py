#!/usr/bin/python3.6
# -*- coding:utf-8 -*-
# https://leetcode.com/problems/arithmetic-slices/


class Solution:
    def numberOfArithmeticSlices1(self, A):         # 暴力法
        n = len(A)
        count = 0
        for i in range(n - 2):
            d = A[i + 1] - A[i]
            for j in range(i + 2, n):
                for k in range(j, n):
                    if A[k] - A[k - 1] != d:
                        break
                    else:
                        count += 1
                break
        return count

    def numberOfArithmeticSlices2(self, A):  # 暴力法
        n = len(A)
        count = 0
        for i in range(n - 2):
            d = A[i + 1] - A[i]
            for j in range(i + 2, n):
                if A[j] - A[j - 1] == d:
                    count += 1
                else:
                    break
        return count

    def numberOfArithmeticSlices3(self, A):     # 递归
        def compute(A, i):
            if i < 2:
                return 0
            ap = 0
            if A[i]-A[i-1] == A[i-1]-A[i-2]:
                ap = 1 + compute(A, i-1)
            return ap
        n = len(A)
        count = 0
        for i in range(n-1, 1, -1):
            count += compute(A, i)
        return count

    def numberOfArithmeticSlices4(self, A):     # 动态规划 时间复杂度为O(n)，空间复杂度为O(n)
        n = len(A)
        dp = [0]*n
        count = 0
        for i in range(2, n):
            if A[i] - A[i-1] == A[i-1] - A[i-2]:
                dp[i] = 1+dp[i-1]
                count += dp[i]
        return count

    def numberOfArithmeticSlices5(self, A):
        n = len(A)
        count = 0
        dp = 0
        for i in range(2, n):
            if A[i] - A[i-1] == A[i-1] - A[i-2]:
                dp += 1
                count += dp
            else:
                dp = 0
        return count


if __name__ == '__main__':
    s = Solution()
    nums = [2, 1, 3, 4, 2, 3]
    nums1 = [1, 2, 3, 4, 5, 6]
    print(s.numberOfArithmeticSlices5(nums1))
