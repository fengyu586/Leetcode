# -*- coding: utf-8 -*-
# @Author  : Jing
# @FileName: 对称二叉树.py
# @IDE: PyCharm


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def is_symmetrical(self, left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        if left.val != right.val:
            return False
        return self.is_symmetrical(left.left, right.right) and self.is_symmetrical(left.right, right.left)

    def isSymmetrical(self, pRoot):
        # write code here
        if not pRoot:
            return True
        else:
            return self.is_symmetrical(pRoot.left, pRoot.right)



