# -*- coding: utf-8 -*-
# @Author  : Jing
# @FileName: 39.数组中出现次数超过一半的数字.py
# @IDE: PyCharm


class Solution:
    def location(self, numbers, start, end):
        val = numbers[start]
        while start < end:
            while start < end and numbers[end] >= val:
                end -= 1
            numbers[start] = numbers[end]
            while start < end and numbers[start] < val:
                start += 1
            numbers[end] = numbers[start]
        numbers[start] = val
        return start

    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        if not numbers:
            return 0
        mid = (len(numbers)) >> 1
        n = len(numbers)
        index = self.location(numbers, 0, n - 1)
        while index != mid:
            if index < mid:
                index = self.location(numbers, index+1, n - 1)
            else:
                index = self.location(numbers, 0, index-1)
        val = numbers[index]
        count = 0
        for i in numbers:
            if i == val:
                count += 1
        if count > mid:
            return val
        else:
            return 0


if __name__ == '__main__':
    nums = [1, 2, 3, 2, 2, 2, 5, 4, 2]
    s = Solution()
    print(s.MoreThanHalfNum_Solution(nums))

