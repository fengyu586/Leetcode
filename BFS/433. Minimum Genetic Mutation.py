#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""====================================
# @Time    : 2019/8/1 22:53
# @Author  : Jing
# @FileName: 433. Minimum Genetic Mutation.py
# @IDE: PyCharm
======================================="""
# https://leetcode.com/problems/minimum-genetic-mutation/

# similar to 127
class Solution:
    def minMutation(self, start, end, bank):
        from collections import defaultdict
        if len(bank) == 0 or bank is None:
            return -1
        all_combo_dict = defaultdict(list)
        l = len(start)
        for mid in bank:
            for i in range(l):
                all_combo_dict[mid[:i]+'*'+mid[i+1:]].append(mid)
        queue = [(start, 0)]
        visited = {start: True}
        while queue:
            cur, level = queue.pop(0)
            for i in range(l):
                for mid in all_combo_dict[cur[:i]+'*'+cur[i+1:]]:
                    if mid == end:
                        return level+1
                    if mid not in visited:
                        visited[mid] = True
                        queue.append((mid, level+1))
        return -1



