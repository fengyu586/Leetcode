# -*- coding: utf-8 -*-
# @Author  : Jing
# @FileName: 1014. Best Sightseeing Pair.py
# @IDE: PyCharm
# https://leetcode.com/problems/best-sightseeing-pair/


class Solution:
    def maxScoreSightseeingPair(self, A):
        if not A:
            return 0
        m, M = 0, 0
        for i in range(1, len(A)):
            m = max(m, A[i-1]+i-1)
            M = max(M, m+A[i]-i)
        return M


if __name__ == '__main__':
    nums = [8, 1, 5, 2, 6]
    s = Solution()
    print(s.maxScoreSightseeingPair(nums))
