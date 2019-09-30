# -*- coding: utf-8 -*-
# @Author  : Jing
# @FileName: 11.旋转数组的最小数字.py
# @IDE: PyCharm
# 题目：把一个数组最开始的若干个元素搬到数组末尾，
# 我们称之为数组的旋转。输入一个递增排序的数组的一个旋转，
# 输出旋转数组的最小元素。
# 例如，数组{3，4，5，1，2}为{1，2，3，4，5}的一个旋转，
# 该数组的最小值为1


def find_min(nums):
    if not nums:
        return None
    n = len(nums)
    left, right = 0, n-1
    min_idx = left
    while nums[left] >= nums[right]:
        if right - left == 1:
            min_idx = right
            break
        min_idx = left+(right-left)//2
        if nums[right] == nums[left] and nums[min_idx] == nums[right]:
            min_idx = left
            for i in range(left, right+1):
                if nums[min_idx] > nums[i]:
                    min_idx = i
            return nums[min_idx]
        if nums[min_idx] >= nums[left]:
            left = min_idx
        elif nums[min_idx] <= nums[right]:
            right = min_idx
    return nums[min_idx]


if __name__ == '__main__':
    nums = [3, 4, 5, 1, 2]
    print(find_min(nums))



