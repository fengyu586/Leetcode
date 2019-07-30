#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""====================================
# @Time    : 2019/7/30 17:28
# @Author  : Jing
# @FileName: 102. Binary Tree Level Order Traversal.py
# @IDE: PyCharm
======================================="""
# https://leetcode.com/problems/binary-tree-level-order-traversal/


class Solution:
    def levelOrder0(self, root):
        if not root:
            return []
        stack, res, count = [root], [[root.val]], 1
        while stack:
            tmp = stack.pop(0)
            if tmp.left:
                stack.append(tmp.left)
            if tmp.right:
                stack.append(tmp.right)
            count -= 1
            if count == 0:
                queue = [x.val for x in stack]
                res += [queue] if queue else []
                count = len(stack)
        return res

    def levelOrder1(self, root):
        if root is None:
            return []
        res, cur = [], [root]
        while cur:
            tmp, new = [], []
            for node in cur:
                tmp.append(node.val)
                if node.left:
                    new.append(node.left)
                if node.right:
                    new.append(node.right)
            res.append(tmp)
            cur = new
        return res





