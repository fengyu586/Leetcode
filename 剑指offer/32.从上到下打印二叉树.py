# -*- coding: utf-8 -*-
# @Author  : Jing
# @FileName: 32.从上到下打印二叉树.py
# @IDE: PyCharm


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        if not root:
            return []
        if not isinstance(root, TreeNode):
            return []
        deque = [root]
        res = []
        while deque:
            node = deque.pop(0)
            res.append(node.val)
            if node.left:
                deque.append(node.left)
            if node.right:
                deque.append(node.right)
        return res
