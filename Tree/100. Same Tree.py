# -*- coding: utf-8 -*-
# @Author  : Jing
# @FileName: 100. Same Tree.py
# @IDE: PyCharm
# https://leetcode.com/problems/same-tree/
from base import TreeNode, reConstructBinaryTree, PrintTree


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


if __name__ == '__main__':
    pre_order = [1, 2, 3]
    in_order = [2, 1, 3]
    root = reConstructBinaryTree(pre_order, in_order)
    p = PrintTree()
    p.pre_order(root)
    p.print_tree()
    s = Solution()
    print(s.isSameTree(root, root))
