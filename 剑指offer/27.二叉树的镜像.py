# -*- coding: utf-8 -*-
# @Author  : Jing
# @FileName: 27.二叉树的镜像.py
# @IDE: PyCharm


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        # write code here
        if not root:
            return None
        if not root.left and not root.right:
            return None
        root.left, root.right = root.right, root.left
        if root.left:
            self.Mirror(root.left)
        if root.right:
            self.Mirror(root.right)