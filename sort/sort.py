#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""====================================
# @Time    : 2019/8/15 20:01
# @Author  : Jing
# @FileName: sort.py
# @IDE: PyCharm
======================================="""
import time


def bubble_sort(lists):
    """冒泡排序"""
    n = len(lists)
    for i in range(n):
        for j in range(i+1, n):
            if lists[j] < lists[j-1]:
                lists[j], lists[j-1] = lists[j-1], lists[j]
    return lists


def select_sort(lists):
    """选择排序"""
    n = len(lists)
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if lists[min_index] > lists[j]:
                lists[min_index], lists[j] = lists[j], lists[min_index]
    return lists


def insert_sort(lists):
    """插入排序"""
    n = len(lists)
    for i in range(1, n):
        j = i
        while j > 0:
            if lists[j] < lists[j-1]:
                lists[j], lists[j-1] = lists[j-1], lists[j]
                j -= 1
            else:
                break
    return lists


def shell_sort0(lists):
    """希尔排序"""
    n = len(lists)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            j = i
            while j > 0:
                if lists[j] < lists[j-gap]:
                    lists[j], lists[j-gap] = lists[j-gap], lists[j]
                    j -= gap
                else:
                    break
        gap = gap // 2
    return lists


def shell_sort1(lists):         # better
    """希尔排序"""
    n = len(lists)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            j = i
            while j >= gap:
                if lists[j] < lists[j-gap]:
                    lists[j], lists[j-gap] = lists[j-gap], lists[j]
                    j -= gap
                else:
                    break
        gap = gap // 2
    return lists


def quick_sort(lists, first, last):
    """快速排序"""
    if first >= last:
        return
    mid_val = lists[first]
    low, high = first, last
    while low < high:
        # high 左移
        while low < high and lists[high] >= mid_val:
            high -= 1
        lists[low] = lists[high]
        # low 右移
        while low < high and lists[low] < mid_val:
            low += 1
        lists[high] = lists[low]
    lists[low] = mid_val
    # 对low左边的列表进行排序
    quick_sort(lists, first, low-1)
    # 对low右边的列表进行排序
    quick_sort(lists, low+1, last)


def merge_sort(lists):
    """归并排序"""
    n = len(lists)
    if n <= 1:
        return lists
    mid = n // 2
    # left 采用的是归并排序后新的列表
    left_li = merge_sort(lists[:mid])
    # right 采用的是归并排序后新的列表
    right_li = merge_sort(lists[mid:])
    # 将两个有序的子序列合并为一个新的整体
    left_pointer, right_pointer = 0, 0
    result = []
    while left_pointer < len(left_li) and right_pointer < len(right_li):
        if left_li[left_pointer] < right_li[right_pointer]:
            result += [left_li[left_pointer]]
            left_pointer += 1
        else:
            result += [right_li[right_pointer]]
            right_pointer += 1
    result += left_li[left_pointer:]
    result += right_li[right_pointer:]
    return result


def test(lists):
    tmp1 = []
    tmp2 = []
    tmp3 = []
    tmp4 = []
    tmp5 = []
    tmp6 = []
    start = time.time()
    for i in range(100000):
        tmp5 = bubble_sort(lists)
    end = time.time()
    print("bubble_sort use time: %gs" % (end - start))
    print(tmp5)
    start = time.time()
    for i in range(100000):
        tmp6 = select_sort(lists)
    end = time.time()
    print("select_sort use time: %gs" % (end - start))
    print(tmp6)
    start = time.time()
    for i in range(100000):
        tmp1 = shell_sort0(lists)
    end = time.time()
    print("shell_sort0 use time: %gs" % (end - start))
    print(tmp1)
    start = time.time()
    for i in range(100000):
        tmp2 = shell_sort1(lists)
    end = time.time()
    print("shell_sort1 use time: %gs" % (end - start))
    print(tmp2)
    start = time.time()
    for i in range(100000):
        tmp3 = shell_sort0(lists)
    end = time.time()
    print("insert_sort use time: %gs" % (end - start))
    print(tmp3)
    start = time.time()
    for i in range(100000):
        tmp4 = merge_sort(lists)
    end = time.time()
    print("merge_sort use time: %gs" % (end - start))
    print(tmp4)
    # start = time.time()
    # for i in range(100000):
    #     quick_sort(lists, 0, len(lists)-1)
    # end = time.time()
    # print("quick_sort use time: %gs" % (end - start))
    # print(lists)


class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution:
    def quick_sort(self, nums, first, last):
        if first >= last:
            return
        mid_val = nums[first]
        low, high = first, last
        while low < high:
            while low < high and nums[high].start >= mid_val.start:
                high -= 1
            nums[low] = nums[high]
            while low < high and nums[low].start < mid_val.start:
                low += 1
            nums[high] = nums[low]
        nums[low] = mid_val
        self.quick_sort(nums, first, low - 1)
        self.quick_sort(nums, low + 1, last)

    def merge(self, intervals):
        self.quick_sort(intervals, 0, len(intervals) - 1)
        merged = []
        for interval in intervals:
            if not merged or merged[-1].end < interval.start:
                merged.append(interval)
            else:
                merged[-1].start = max(merged[-1].start, interval.end)
        return merged


def maopao(dic):
    li = [i for i in dic.values()]
    sorted(li, key=lambda x: x[-1], reverse=True)
    for i in li:
        i[-1] = str(i[-1])
    if len(li) > 8:
        for i in li[0:8]:
            print(' '.join(i))
    else:
        for i in li:
            print(' '.join(i))


if __name__ == '__main__':
    a = [3, 5, 9, 25, 61, 23, 0, 72, 15, 36, 52]
    b = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    # print(insert_sort(a))
    test(a)
    # c = [Interval(1, 3), Interval(2, 6), Interval(8, 10), Interval(15, 18)]
    # d = Solution()
    # d.quick_sort(c, 0, len(c)-1)
    # for m in c:
    #     print(m.start, m.end)