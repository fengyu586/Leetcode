# -*- coding: utf-8 -*-
# @Author  : Jing
# @FileName: 81. Search in Rotated Sorted Array II.py
# @IDE: PyCharm
# https://leetcode.com/problems/search-in-rotated-sorted-array-ii/
# Solution 1: O(n)Time, O(1)Space
# Solution 2: O(n)Time, O(1)Space


class Solution:
    def search1(self, nums, target):
        if not nums:
            return False
        for num in nums:
            if num == target:
                return True
        return False

    def search2(self, nums, target):
        if not nums:
            return False
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left+right) >> 1
            if nums[mid] == target:
                return True
            if nums[left] == nums[mid] == nums[right]:
                left += 1
                right -= 1

            # 在前一部分
            elif nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid-1
                else:
                    left = mid+1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid+1
                else:
                    right = mid-1
        return False



if __name__ == '__main__':
    nums = [1, 3, 5]
    target = 1
    s = Solution()
    print(s.search2(nums, target))




