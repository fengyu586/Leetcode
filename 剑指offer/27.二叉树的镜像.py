# -*- coding: utf-8 -*-
# @Author  : Jing
# @FileName: 27.二叉树的镜像.py
# @IDE: PyCharm
# Solution 1: Recursively
# Solution 2: Iteratively

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回镜像树的根节点
    def Mirror1(self, root):
        # write code here
        if not root:
            return None
        if not root.left and not root.right:
            return None
        root.left, root.right = root.right, root.left
        if root.left:
            self.Mirror1(root.left)
        if root.right:
            self.Mirror1(root.right)

    def Mirror12(self, root):
        # write code here
        if not root:
            return None
        if not root.left and not root.right:
            return root
        stack = [root]
        while stack:
            node = stack.pop()
            node.left, node.right = node.right, node.left
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return root