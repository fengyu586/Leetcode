#!/usr/bin/python3.6
# -*- coding:utf-8 -*-
# https://leetcode.com/problems/container-with-most-water/
# maxArea1 is two point approach
# maxArea2 暴力法 result: Time Limit Exceeded


class Solution:
    def maxArea1(self, height):
        n = len(height)
        max_area = 0
        start, end = 0, n-1
        while end != start:
            max_area = max(min(height[start], height[end])*(end-start), max_area)
            if height[end] > height[start]:
                start += 1
            else:
                end -= 1
        return max_area

    def maxArea2(self, height):
        max_area = 0
        n = len(height)
        for i in range(n):
            for j in range(i+1, n):
                max_area = max(min(height[i], height[j])*(j-i), max_area)
        return max_area


print(2)

