# -*- coding: utf-8 -*-
# @Author  : Jing
# @FileName: 110. Balanced Binary Tree.py
# @IDE: PyCharm
# https://leetcode.com/problems/balanced-binary-tree/
from base import TreeNode, reConstructBinaryTree, PrintTree


class Solution:
    def __init__(self):
        self.flag = True

    def maxDepth(self, root):
        if not root:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        if abs(left - right) > 1:
            self.flag = False
        return max(left, right) + 1

    def isBalanced(self, root: TreeNode) -> bool:
        self.maxDepth(root)
        return self.flag


if __name__ == '__main__':
    pre_order, in_order = [1, 2, 3, 4, 4, 3, 2], [4, 3, 4, 2, 3, 1, 2]
    root = reConstructBinaryTree(pre_order, in_order)
    s = Solution()
    p = PrintTree()
    p.pre_order(root)
    p.print_tree()
    print(s.isBalanced(root))
