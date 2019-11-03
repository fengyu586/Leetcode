# -*- coding: utf-8 -*-
# @Author  : Jing
# @FileName: 50.第一个只出现一次的字符.py
# @IDE: PyCharm
# Solution 1: map O(n)Time O(n)Space


class Solution:
    def first_one(self, nums):
        dic = {}
        for num in nums:
            if num not in dic:
                dic[num] = 1
            else:
                dic[num] += 1
        for num in dic.keys():
            if dic[num] == 1:
                return num
        return -1


if __name__ == '__main__':
    nums = [0, 1, 1, 2, 2]
    s = Solution()
    print(s.first_one(nums))
