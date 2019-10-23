# -*- coding: utf-8 -*-
# @Author  : Jing
# @FileName: 45.把数组排成最小的数.py
# @IDE: PyCharm


class Solution:
    def compare_string(self, str1, str2):
        n = len(str1)
        m = len(str2)
        if m != n:
            raise Exception("the length is not same!")
        for i in range(n):
            if str1[i] > str2[i]:
                return True
            elif str1[i] < str2[i]:
                return False
        return True

    def qsort(self, nums, start, end):
        if start >= end:
            return
        left, right = start, end
        baseline = nums[left]
        while left < right:
            while left < right and self.compare_string(nums[right]+baseline, baseline+nums[right]):
                right -= 1
            nums[left] = nums[right]
            while left < right and self.compare_string(baseline+nums[left], nums[left]+baseline):
                left += 1
            nums[right] = nums[left]
        nums[left] = baseline
        self.qsort(nums, start, left-1)
        self.qsort(nums, left+1, end)


    def PrintMinNumber(self, nums, length):
        if not nums or len(nums) != length:
            return -1
        nums = list(map(str, nums))
        start, end = 0, len(nums)-1
        self.qsort(nums, start, end)
        string = ''.join(nums)
        return string


if __name__ == '__main__':
    nums = [3, 323, 32123]
    s = Solution()
    print(s.PrintMinNumber(nums, len(nums)))
