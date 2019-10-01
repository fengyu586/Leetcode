# -*- coding: utf-8 -*-
# @Author  : Jing
# @FileName: quick_sort.py
# @IDE: PyCharm


# def Partition(nums, length, start, end):
#     if nums is None or length <=0 or start < 0 or end >= length or end < start:
#         raise Exception("Invalid Parameters")
#     mid = (start+end)>>1
#     mid_val = nums[mid]
#     while start < end:
#         while start < end and nums[end] >= mid_val:
#             end -= 1
#         nums[mid] = nums[end]
#         while start < end and nums[start] < mid_val:
#             start += 1
#         nums[end] = nums[start]
#         start += 1
#         end -= 1
#         nums[start], nums[end] = nums[end], nums[start]
#     nums[start] = mid_val
#     print(nums)
#     return start
#
#
# def quick_sort(nums, length, start, end):
#     if start == end:
#         return
#     index = Partition(nums, length, start, end)
#     if index > start:
#         quick_sort(nums, length, start, index-1)
#     if index < end:
#         quick_sort(nums, length, index+1, end)
#
#
# if __name__ == '__main__':
#     nums = [8, 5, 9, 7, 1, 2, 4, 3]
#     length = len(nums)
#     start, end = 0, length-1
#     quick_sort(nums, length, start, end)


