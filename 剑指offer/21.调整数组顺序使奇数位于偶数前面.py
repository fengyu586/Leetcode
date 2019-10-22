# -*- coding: utf-8 -*-
# @Author  : Jing
# @FileName: 21.调整数组顺序使奇数位于偶数前面.py
# @IDE: PyCharm

class Solution:
    def isEven(self, num):
        flag = num & 0x1 == 0
        return flag

    def ReorderOddEven(self, nums, length):
        if length <= 0:
            return nums
        start, end = 0, length-1
        while start < end:
            while start < end and not self.isEven(nums[start]):
                start += 1
            while start < end and self.isEven(nums[end]):
                end -= 1
            if start < end:
                nums[start], nums[end] = nums[end], nums[start]
        return nums


if __name__ == '__main__':
    nums = list(range(1, 6))
    s = Solution()
    print(s.ReorderOddEven(nums, len(nums)))


