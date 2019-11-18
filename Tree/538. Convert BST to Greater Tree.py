# -*- coding: utf-8 -*-
# @Author  : Jing
# @FileName: 538. Convert BST to Greater Tree.py
# @IDE: PyCharm
# https://leetcode.com/problems/convert-bst-to-greater-tree/
from base import TreeNode, reConstructBinaryTree, PrintTree


class Solution:
    def __init__(self):
        self.sum = 0

    def helper(self, root):
        if not root:
            return 0
        self.sum = self.helper(root.left) + root.val + self.helper(root.right)
        return self.sum

    def helper1(self, root):
        if root:
            if root.left:
                self.helper1(root.left)
            root.val, self.sum = self.sum, self.sum - root.val
            if root.right:
                self.helper1(root.right)

    def convertBST(self, root: TreeNode) -> TreeNode:
        self.helper(root)
        self.helper1(root)
        return root


if __name__ == '__main__':
    pre_order = [5, 2, 13]
    in_order = [2, 5, 3]
    root = reConstructBinaryTree(pre_order, in_order)
    p = PrintTree()
    p.pre_order(root)
    p.print_tree()
    s = Solution()
    root = s.convertBST(root)
    p.pre_order(root)
    p.print_tree()

