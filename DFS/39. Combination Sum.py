#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""====================================
# @Time    : 2019/8/11 11:24
# @Author  : Jing
# @FileName: 39. Combination Sum.py
# @IDE: PyCharm
======================================="""
# https://leetcode.com/problems/combination-sum/
# 1 steps: delete duplicate
# 2 steps: target


class Solution:
    # 递归的定义
    # 找到所有以combination 开头的那些和为target的组合
    # 并丢到res里，其中剩余的需要加入combination里的数为remainTarget
    # 并且下一个可以加入combination中的数，至少从candidates的startIndex开始
    def recursion(self, candidates, startIndex, remainTarget, combination, results):
        # 递归的出口
        if remainTarget == 0:
            results.append([i for i in combination])
            return

            # 递归的拆解
        for i in range(startIndex, len(candidates)):
            if remainTarget < candidates[i]:
                break
            combination.append(candidates[i])
            self.recursion(candidates, i, remainTarget - candidates[i], combination, results)
            combination.pop()

    def combinationSum(self, candidates, target):
        results = []
        if not candidates:
            return results
        combination = []
        candidates = list(set(candidates))
        candidates = sorted(candidates)
        self.recursion(candidates, 0, target, combination, results)
        return results


if __name__ == '__main__':
    a = [2,3,6,7]
    target = 7
    s = Solution()
    print(s.combinationSum(a, target))              # Output is [[2, 2, 3], [7]].


