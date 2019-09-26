# -*- coding: utf-8 -*-
# @Author  : Jing
# @FileName: 3. 数组中重复的数字.py
# @IDE: PyCharm
# Solution 1：排序+遍历 O(nlogn)Time O(1)Space
# Solution 2: 哈希表 O(n)Time O(n)Space
# Solution 3: O(n)Time O(1)Space, 仅能找出一个
# 数组的特点：长度为n，数组中所有的数字均在0~n-1的范围内

class Solution:
    def duplicate1(self, nums):
        if nums is None or len(nums) == 0:
            return None
        if max(nums) > len(nums) or min(nums) < 0:
            return None
        nums = sorted(nums)
        res = set()
        for i in range(1, len(nums)):
            if nums[i-1] == nums[i]:
                res.add(nums[i])
        return list(res)

    def duplicate2(self, nums):
        if nums is None or len(nums) == 0:
            return None
        if max(nums) > len(nums) or min(nums) < 0:
            return None
        tmp = dict()
        res = set()
        for i in nums:
            if i not in tmp:
                tmp[i] = 1
            else:
                res.add(i)
        return list(res)

    def duplicate3(self, nums):
        if nums is None or len(nums) == 0:
            return None
        if max(nums) > len(nums) or min(nums) < 0:
            return None
        res = set()
        for i in range(len(nums)):
            while nums[i] != i:
                tmp = nums[i]
                if tmp == nums[tmp]:
                    res.add(tmp)
                    break
                nums[i], nums[tmp] = nums[tmp], nums[i]
        return list(res)


if __name__ == '__main__':
    nums = [2, 3, 1, 0, 2, 5, 3]
    s = Solution()
    print(s.duplicate3(nums))       # Output is [2, 3]