#!/usr/bin/python3.6
# -*- coding:utf-8 -*-
# https://leetcode.com/problems/maximum-gap/


class Solution:
    def bubble_sort(self, nums, n):
        for i in range(n-2, -1, -1):
            for j in range(i + 1, n):
                if nums[j - 1] > nums[j]:
                    nums[j - 1], nums[j] = nums[j], nums[j - 1]
        return nums

    def fast_sort(self, nums, first, last):
        if first >= last:
            return
        l, r = first, last
        mid_val = nums[l]
        while l < r:
            while l < r and nums[r] >= mid_val:
                r -= 1
            nums[l] = nums[r]
            while l < r and nums[l] < mid_val:
                l += 1
            nums[r] = nums[l]
        nums[l] = mid_val
        self.fast_sort(nums, first, l - 1)
        self.fast_sort(nums, l + 1, last)



    def maximumGap(self, nums):
        n = len(nums)
        if n < 2:
            return 0
        max_diff = 0
        self.fast_sort(nums, 0, n-1)
        print(nums)
        # nums.sort()
        for i in range(1, n):
            if nums[i] - nums[i - 1] > max_diff:
                max_diff = nums[i] - nums[i - 1]
        return max_diff


def main():
    s = Solution()
    nums = [100, 2, 3, 1]
    print(s.maximumGap(nums))


if __name__ == '__main__':
    main()

