# -*- coding: utf-8 -*-
# @Author  : Jing
# @FileName: 数据流中的中位数.py
# @IDE: PyCharm


class Solution:
    def __init__(self):
        self.nums = []

    def Insert(self, num):
        # write code here
        self.nums.append(float(num))

    def location(self, start, end):
        left, right = start, end
        num = self.nums[left]
        while left < right:
            while left < right and self.nums[right] >= num:
                right -= 1
            self.nums[left] = self.nums[right]
            while left < right and self.nums[left] < num:
                left += 1
            self.nums[right] = self.nums[left]
        self.nums[left] = num
        return left

    def GetMedian(self, data):
        # write code here
        n = len(self.nums)
        start, end = 0, n - 1
        mid = (start + end) >> 1
        index = 0
        while index >= 0 and index < n and index != mid:
            index = self.location(start, end)
            if index > mid:
                end = index - 1
            else:
                start = index + 1
        if n % 2 != 0:
            return self.nums[index]
        else:
            num1 = self.nums[index]
            start, end = mid + 1, n - 1
            while index >= 0 and index < n and index != mid + 1:
                index = self.location(start, end)
                if index > mid:
                    end = index - 1
                else:
                    start = index + 1
            num2 = self.nums[index]
            return (num1 + num2) / 2.0


if __name__ == '__main__':
    nums = [5, 2, 3, 1, 6, 7, 0, 8]
    s = Solution()
    for i in range(8):
        s.Insert(nums[i])
        print(s.GetMedian(i))
