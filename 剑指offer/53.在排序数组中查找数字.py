# -*- coding: utf-8 -*-
# @Author  : Jing
# @FileName: 53.在排序数组中查找数字.py
# @IDE: PyCharm
# Solution 1: Sequential traversal O(n)Time O(1)Space
# Solution 2: Binary search O(logn)Time O(1)Space


class Solution:
    def GetNumberOfK1(self, data, k):
        # write code here
        if not data:
            return 0
        n = len(data)
        p1 = 0
        while p1 != n:
            if data[p1] != k:
                p1 += 1
            else:
                break
        p2 = p1
        while p2 != n:
            if data[p2] == k:
                p2 += 1
            else:
                break
        number = p2-p1
        return number

    def GetNumberOfK2(self, data, k):
        if not data:
            return 0
        n = len(data)
        left, right = 0, n-1
        mid = 0
        while left <= right:
            mid = (left + right) // 2
            if data[mid] == k:
                break
            elif data[mid] > k:
                right = mid-1
            else:
                left = mid+1
        if data[mid] != k:
            return 0
        p1, p2 = mid, mid
        while p1 >= 0 and data[p1] == k:
            p1 -= 1
        p1 += 1
        while p2 < n and data[p2] == k:
            p2 += 1
        number = p2-p1
        return number


if __name__ == '__main__':
    nums = [1, 2, 3, 3, 3, 3, 4]
    k = 5
    s = Solution()
    print(s.GetNumberOfK2(nums, k))