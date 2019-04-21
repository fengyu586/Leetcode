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

    def insert_sort(self, nums):
        n = len(nums)
        for i in range(1, n):
            for j in range(i, 0, -1):
                if nums[j - 1] > nums[j]:
                    nums[j - 1], nums[j] = nums[j], nums[j - 1]
        return nums

    def select_sort(self, nums):
        n = len(nums)
        for i in range(n):
            min_val = nums[i]
            min_index = i
            for j in range(i+1, n):
                if nums[j] < min_val:
                    min_val = nums[j]
                    min_index = j
            nums[i], nums[min_index] = nums[min_index], nums[i]
        return nums

    def shell_sort(self, nums):
        n = len(nums)
        gap = n//2
        while gap > 0:
            for i in range(gap, n):
                j = i
                while j >= gap:
                    if nums[j-gap] > nums[j]:
                        nums[j-gap], nums[j] = nums[j], nums[j-gap]
                        j -= gap
                    else:
                        break
            gap //= 2
        return nums

    def merge_sort(self, nums):
        n = len(nums)
        if n <= 1:
            return nums
        mid = n//2
        l_li = self.merge_sort(nums[0:mid])
        r_li = self.merge_sort(nums[mid:])
        res = []
        l_pointer, r_pointer = 0, 0
        while l_pointer < len(l_li) and r_pointer < len(r_li):
            if l_li[l_pointer] < r_li[r_pointer]:
                res += [l_li[l_pointer]]
                l_pointer += 1
            else:
                res += [r_li[r_pointer]]
                r_pointer += 1
        res += l_li[l_pointer:]
        res += r_li[r_pointer:]
        return res

    def maximumGap(self, nums):
        n = len(nums)
        if n < 2:
            return 0
        max_diff = 0
        nums = self.merge_sort(nums)
        # self.shell_sort(nums)
        # self.select_sort(nums)
        # self.insert_sort(nums)
        # self.fast_sort(nums, 0, n-1)
        print(nums)
        # nums.sort()
        for i in range(1, n):
            if nums[i] - nums[i - 1] > max_diff:
                max_diff = nums[i] - nums[i - 1]
        return max_diff


def main():
    import random
    s = Solution()
    nums = [100, 2, 3, 1]
    nums1 = [random.randint(1, 20) for _ in range(20)]
    print(s.maximumGap(nums1))


if __name__ == '__main__':
    main()

