# -*- coding: utf-8 -*-
# @Author  : Jing
# @FileName: 219. Contains Duplicate II.py
# @IDE: PyCharm
# https://leetcode.com/problems/contains-duplicate-ii/


class Solution:
    def containsNearbyDuplicate(self, nums, k):
        dic = {}
        for i, num in enumerate(nums):
            if num in dic and i-dic[num] <= k:
                return True
            dic[num] = i
        return False


if __name__ == '__main__':
    s = Solution()
    nums, k = [1, 2, 3, 1], 3
    print(s.containsNearbyDuplicate(nums, k))           # Output is True
