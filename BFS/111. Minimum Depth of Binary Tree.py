#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""====================================
# @Time    : 2019/7/30 17:56
# @Author  : Jing
# @FileName: 111. Minimum Depth of Binary Tree.py
# @IDE: PyCharm
======================================="""
# https://leetcode.com/problems/minimum-depth-of-binary-tree/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        queue = [(root, 1)]
        while queue:
            node, level = queue.pop(0)
            if node:
                if node.left is None and node.right is None:
                    return level
                else:
                    queue.append((node.left, level+1))
                    queue.append((node.right, level+1))








