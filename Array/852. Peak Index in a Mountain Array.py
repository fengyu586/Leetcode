# -*- coding: utf-8 -*-
# @Author  : Jing
# @FileName: 852. Peak Index in a Mountain Array.py
# @IDE: PyCharm
# https://leetcode.com/problems/peak-index-in-a-mountain-array/


class Solution:
    def peakIndexInMountainArray(self, A):
        if not A:
            return -1
        l, r = 0, len(A) - 1
        while l <= r:
            mid = (l+r) >> 1
            if A[mid] < A[mid-1]:
                r = mid - 1
            elif A[mid] < A[mid+1]:
                l = mid + 1
            else:
                return mid
        return -1


if __name__ == '__main__':
    nums = [0, 1, 0]
    s = Solution()
    print(s.peakIndexInMountainArray(nums))
