#!/usr/bin/python3.6
# -*- coding:utf-8 -*-
# https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height):
        n = len(height)
        max_val = 0
        start, end = 0, n-1
        while end != start:
            max_val = max(min(height[start], height[end])*(end-start), max_val)
            if height[end] > height[start]:
                start += 1
            else:
                end -= 1
        return max_val







