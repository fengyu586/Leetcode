# -*- coding: utf-8 -*-
# @Author  : Jing
# @FileName: 80. Remove Duplicates from Sorted Array II.py
# @IDE: PyCharm
# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
# Solution : O(n)Time O(1)Space


class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        length = len(nums)
        index = length - 1
        count = 1
        tmp = nums[index]
        while index > 0:
            index -= 1
            if nums[index] == tmp:
                count += 1
                if count > 2:
                    nums.remove(nums[index])
            else:
                count = 1
                tmp = nums[index]
        return len(nums)


if __name__ == '__main__':
    nums = [1, 1, 1, 2, 2, 3]
    s = Solution()
    print(s.removeDuplicates(nums))

