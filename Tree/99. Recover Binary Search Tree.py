# -*- coding: utf-8 -*-
# @Author  : Jing
# @FileName: 99. Recover Binary Search Tree.py
# @IDE: PyCharm
# https://leetcode.com/problems/recover-binary-search-tree/
from base import TreeNode, reConstructBinaryTree, pre_order
import sys


class Solution:
    def __init__(self):
        self.first = None
        self.second = None
        self.preNode = None
        self.root = None

    def orderTraveral(self, root):
        if not root:
            return
        self.orderTraveral(root.left)
        if not self.first and self.preNode.val > root.val:
            self.first, self.second = self.preNode, root
        if self.first and self.preNode and self.preNode.val < root.val:
            self.second = root
        self.preNode = root
        self.orderTraveral(root.right)

    def recoverTree(self, root: TreeNode):
        """
        Do not return anything, modify root in-place instead.
        """
        self.root = root
        self.preNode = TreeNode(-sys.maxsize-1)
        self.orderTraveral(root)
        self.first.val, self.second.val = self.second.val, self.first.val
        return self.root


if __name__ == '__main__':
    preOrder = [3, 1, 4, 2]
    inOrder = [1, 3, 2, 4]
    root = reConstructBinaryTree(preOrder, inOrder)
    s = Solution()
    root = s.recoverTree(root)
    print(pre_order(root))
