# -*- coding: utf-8 -*-
# @Author  : Jing
# @FileName: 56.数组中数字出现的次数.py
# @IDE: PyCharm
# https://leetcode.com/problems/single-number/
# https://leetcode.com/problems/single-number-ii/
# https://leetcode.com/problems/single-number-iii/
# Solution 1:   dict    O(n)Time    O(n)Space
# Solution 2:   xor     O(n)Time    O(1)Space
# Solution 3:   dict    O(n)Time    O(n)Space
# Solution 4:   math    O(n)Time    O(n)Space
# Solution 5:   dict    O(n)Time    O(n)Space
# Solution 6:   xor     O(n)Time    O(1)Space


class Solution:
    def singleNumber1(self, nums):
        if not nums:
            return -1
        dic = {}
        for num in nums:
            dic[num] = dic.get(num, 0) + 1
        for num in nums:
            if dic[num] == 1:
                return num

    def singleNumber2(self, nums):
        if not nums:
            return -1
        xor = 0
        for num in nums:
            xor ^= num
        return xor

    def singleNumber3(self, nums):
        if not nums:
            return -1
        dic = {}
        for num in nums:
            dic[num] = dic.get(num, 0) + 1
        for num in nums:
            if dic[num] == 1:
                return num
        return -1

    def singleNumber4(self, nums):
        if not nums:
            return -1
        return (3*sum(set(nums)) - sum(nums))//2

    def singleNumber5(self, nums):
        res, dic = [], {}
        if not nums:
            return res
        for num in nums:
            dic[num] = dic.get(num, 0) + 1
        for num in nums:
            if dic[num] == 1:
                res.append(num)
        return res

    def singleNumber6(self, nums):
        if not nums:
            return []
        xor = 0
        for num in nums:
            xor ^= num
        mask = 1
        while mask & xor == 0:
            mask <<= 1
        num1, num2 = 0, 0
        for num in nums:
            if mask & num:
                num1 ^= num
            else:
                num2 ^= num
        return [num1, num2]


if __name__ == '__main__':
    nums = [1, 2, 1, 3, 2, 5]
    s = Solution()
    print(s.singleNumber2(nums))

