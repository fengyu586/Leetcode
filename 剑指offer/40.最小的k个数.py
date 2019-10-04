# -*- coding: utf-8 -*-
# @Author  : Jing
# @FileName: 40.最小的k个数.py
# @IDE: PyCharm


def location(nums, start, end):
    left, right = start, end
    baseline = nums[left]
    while left < right:
        while left < right and nums[right] >= baseline:
            right -= 1
        nums[left] = nums[right]
        while left < right and nums[left] < baseline:
            left += 1
        nums[right] = nums[left]
    nums[left] = baseline
    return left

def get_least_numbers(nums, k):
    if not nums or k <= 0:
        return None
    length = len(nums)
    if length < k:
        return None
    res = []
    start, end = 0, length - 1
    while len(res) != k:
        index = location(nums, start, end)
        if index > k-1:
            end = index - 1
        else:
            res += nums[start:index+1]
            start = index+1
    print(res)




if __name__ == '__main__':
    nums = [4, 5, 1, 6, 2, 7, 3, 8]
    get_least_numbers(nums, 4)