#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""====================================
# @Time    : 2019/8/11 15:20
# @Author  : Jing
# @FileName: 40. Combination Sum II.py
# @IDE: PyCharm
======================================="""
# https://leetcode.com/problems/combination-sum-ii/


class Solution:
    def recursion(self, candidates, start_index, remain_target, combination, results):
        if remain_target == 0:
            if combination not in results:
                results.append([i for i in combination])
            return
        for i in range(start_index, len(candidates)):
            if remain_target < candidates[i]:
                break
            combination.append(candidates[i])
            self.recursion(candidates, i + 1, remain_target - candidates[i], combination, results)
            combination.pop()

    def combinationSum2(self, candidates, target):
        if not candidates:
            return candidates
        combination, results = [], []
        candidates = sorted(candidates)
        self.recursion(candidates, 0, target, combination, results)
        return results


if __name__ == '__main__':
    a = [10,1,2,7,6,1,5]
    target = 8
    s = Solution()
    print(s.combinationSum2(a, target))             # Output is [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]

