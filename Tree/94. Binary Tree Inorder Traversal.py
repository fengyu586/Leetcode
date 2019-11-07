# -*- coding: utf-8 -*-
# @Author  : Jing
# @FileName: 94. Binary Tree Inorder Traversal.py
# @IDE: PyCharm
# https://leetcode.com/problems/binary-tree-inorder-traversal/
from base import reConstructBinaryTree


class Solution:
    def __init__(self):
        self.res = []

    def inorder(self, root):
        if not root:
            return None
        if root.left:
            self.inorder(root.left)
        self.res.append(root.val)
        if root.right:
            self.inorder(root.right)
        return

    def inorderTraversal(self, root):
        self.inorder(root)
        return self.res


if __name__ == '__main__':
    preorder = [1, 2, 3]
    inorder_num = [1, 3, 2]
    root = reConstructBinaryTree(preorder, inorder_num)
    s = Solution()
    print(s.inorderTraversal(root))





