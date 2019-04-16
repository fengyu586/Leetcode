#!/usr/bin/python3.6
# -*- coding:utf-8 -*-
# https://leetcode.com/problems/search-a-2d-matrix/


class Solution:
    def searchMatrix(self, matrix, target):
        nums = [i for li in matrix for i in li]
        n = len(nums)
        l, r = 0, n-1
        while l <= r:
            mid = (l+r)//2
            if nums[mid] == target:
                return True
            if nums[mid] > target:
                r = mid-1
            else:
                l = mid+1
        return False


