# -*- coding: utf-8 -*-
# @Author  : Jing
# @FileName: 718. Maximum Length of Repeated Subarray.py
# @IDE: PyCharm
# https://leetcode.com/problems/maximum-length-of-repeated-subarray/
# Solution 1: DP    O(mn)Time O(mn)Space
# Solution 2:


class Solution:
    def findLength(self, A, B) -> int:
        if not A or not B:
            return 0
        m, n = len(A), len(B)
        # dp[i][j] is the length of the longest sub array in A[i:] and B[j:]
        dp = [[0 for _ in range(m+1)] for i in range(n+1)]
        res = 0
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if A[i] == B[j]:
                    dp[i][j] = dp[i+1][j+1] + 1
                    res = max(res, dp[i][j])
        return res


if __name__ == '__main__':
    nums1, nums2 = [1, 2, 3, 2, 1], [3, 2, 1, 4, 7]
    s = Solution()
    print(s.findLength(nums1, nums2))








