#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""====================================
# @Time    : 2019/8/1 20:11
# @Author  : Jing
# @FileName: 103.Binary Tree Zigzag Level Order Traversal.py
# @IDE: PyCharm
======================================="""
# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def zigzagLevelOrder0(self, root):
        res, queue = [], [(root, 0)]
        while queue:
            cur, level = queue.pop(0)
            if cur:
                if len(res) < level+1:
                    res.append([])
                if level % 2 == 0:
                    res[level].append(cur.val)
                else:
                    res[level].insert(0, cur.val)
                if cur.left is not None:
                    queue.append((cur.left, level+1))
                if cur.right is not None:
                    queue.append((cur.right, level+1))
        return res

    # 反向
    def zigzagLevelOrder1(self, root):
        if root is None:
            return root
        res, queue, count = [[root.val]], [(root, 0)], 1
        while queue:
            cur, level = queue.pop(0)
            if cur.left is not None:
                queue.append((cur.left, level + 1))
            if cur.right is not None:
                queue.append((cur.right, level + 1))
            count -= 1
            if count == 0:
                li = [x[0].val for x in queue]
                if level % 2 == 0:
                    res += [li[::-1]] if li else []
                else:
                    res += [li] if li else []
                count = len(queue)
        return res




