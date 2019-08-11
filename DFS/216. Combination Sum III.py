#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""====================================
# @Time    : 2019/8/11 16:41
# @Author  : Jing
# @FileName: 216. Combination Sum III.py
# @IDE: PyCharm
======================================="""
# https://leetcode.com/problems/combination-sum-iii/


class Solution:
    def recursion1(self, remain_num, li, start_index, remain_target, combination, results):
        if remain_num == 0 and remain_target == 0:
            results.append([i for i in combination])
            return

        for i in range(start_index, len(li)):
            if remain_target < li[i]:
                break
            combination.append(li[i])
            self.recursion1(remain_num - 1, li, i + 1, remain_target - li[i], combination, results)
            combination.pop()

    def recursion3(self, nums, k, n, start_index, combination, results):
        if k < 0 or n< 0:
            return
        if k == 0 and n == 0:
            results.append(combination)
        for i in range(start_index, len(nums)):
            self.recursion3(nums, k-1, n-nums[i], i+1, combination+[nums[i]], results)

    def combinationSum1(self, k, n):
        li = [i for i in range(1, 10)]
        if sum(li[:k]) > n or sum(li[9-k:]) < n:
            return None
        combination, results = [], []
        self.recursion1(k, li, 0, n, combination, results)
        return results

    def combinationSum2(self, k, n):
        results = []
        def recursion2(k, n, cur, nxt):
            if len(cur) == k:
                if sum(cur) == n:
                    results.append(cur)
                return
            for i in range(nxt, 10):
                recursion2(k, n, cur + [i], i + 1)
        recursion2(k, n, [], 1)
        return results

    def combinationSum3(self, k, n):
        results = []
        self.recursion3(range(1, 10), k, n, 0, [], results)
        return results


if __name__ == '__main__':
    k, n = 3, 7
    s = Solution()
    print(s.combinationSum3(k, n))              # Output is [[1, 2, 4]].
