# -*- coding: utf-8 -*-
# @Author  : Jing
# @FileName: 1095. Find in Mountain Array.py
# @IDE: PyCharm
# https://leetcode.com/problems/find-in-mountain-array/


class MountainArray:
    def __init__(self, nums):
        self.nums = nums
    def get(self, index: int):
       return self.nums[index]

    def length(self) -> int:
        return len(self.nums)


class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        length = mountain_arr.length()
        if length == 0:
            return -1
        l, r = 1, length - 2
        h = 0
        while l <= r:
            mid = (l + r)>>1
            tmp = mountain_arr.get(mid)
            if tmp < mountain_arr.get(mid-1):
                r = mid - 1
            elif tmp < mountain_arr.get(mid+1):
                l = mid + 1
            else:
                h = mid
                break
        l, r = 0, h
        while l <= r:
            mid = (l+r) >> 1
            val = mountain_arr.get(mid)
            if val == target:
                return mid
            if val > target:
                r = mid - 1
            else:
                l = mid + 1
        l, r = h+1, length - 1
        while l <= r:
            mid = (l + r) >> 1
            val = mountain_arr.get(mid)
            if val == target:
                return mid
            if val > target:
                l = mid + 1
            else:
                r = mid - 1
        return -1


if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 3, 4, 5, 3, 1]
    mountain_arr = MountainArray(nums)
    target = 3
    print(s.findInMountainArray(target, mountain_arr))