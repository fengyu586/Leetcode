# -*- coding: utf-8 -*-
# @Author  : Jing
# @FileName: 1. Two Sum.py
# @IDE: PyCharm
# https://leetcode.com/problems/two-sum/
# Solution 1: Brute Force O(n^2)Time O(1)Space
# Solution 2: Hash O(n)Time O(n)Space scan two time.
# Solution 3: Hash O(n)Time O(n)Space scan one time.


class Solution:
    def twoSum1(self, nums, target):
        if not nums:
            return []
        res = []
        for i in range(len(nums)-1):
            res.append(i)
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j] == target:
                    res.append(j)
                    return res
            res.pop()
        return res

    def twoSum2(self, nums, target):
        if not nums:
            return []
        dic = {}
        for i, num in enumerate(nums):
            if num not in dic:
                dic[num] = [i]
            else:
                dic[num].append(i)
        for key, val in dic.items():
            tmp = target - key
            if tmp == key and len(val) > 1:
                return val[:2]
            elif tmp != key and tmp in dic:
                return [val[0], dic[tmp][0]]
        return []

    def twoSum3(self, nums, target):
        if not nums:
            return []
        dic = {}
        for i, num in enumerate(nums):
            if num not in dic:
                dic[num] = [i]
            else:
                dic[num].append(i)
            tmp = target - num
            if tmp == num and len(dic[num]) > 1:
                return [dic[num][0], i]
            elif tmp in dic and tmp != num:
                return [dic[tmp][0], i]
        return []

if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    s = Solution()
    print(s.twoSum2(nums, target))