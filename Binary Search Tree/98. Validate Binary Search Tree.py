#!/usr/bin/python3.6
# -*- coding:utf-8 -*-
# https://leetcode.com/problems/validate-binary-search-tree/
# Approach 1: recursion
# Approach 2: iteration
# Approach 3: inorder traversal


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST1(self, root):
        # recursion
        def helper(node, lower=float('-inf'), upper=float('inf')):
            if not node:
                return True
            val = node.val
            if val <= lower or val >= upper:
                return False
            if not helper(node.right, val, upper):
                return False
            if not helper(node.left,lower, val):
                return False
            return True
        return helper(root)

        # iteriation
    def isValidBST2(self, root):

        if not root:
            return True
        stack = [(root, float('-inf'), float('inf'))]
        while stack:
            node, lower, upper = stack.pop()
            if not node:
                continue
            if node.val <= lower or node.val >= upper:
                return False
            stack.append((node.right, node.val, upper))
            stack.append((node.left, lower, node.val))
        return True

    def isValidBST3(self, root):
        # inoder traversal
        stack, lower = [], float('-inf')
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if root.val <= lower:
                return False
            lower = root.val
            root = root.right
        return True

















