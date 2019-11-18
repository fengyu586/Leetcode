# -*- coding: utf-8 -*-
# @Author  : Jing
# @FileName: 257. Binary Tree Paths.py
# @IDE: PyCharm
# https://leetcode.com/problems/binary-tree-paths/
from base import TreeNode, reConstructBinaryTree, PrintTree


class Solution:
    def __init__(self):
        self.res = []
    def helper(self, root, cur):
        if not root:
            return None
        if not root.left and not root.right:
            self.res.append([i for i in cur])
        if root.left:
            self.helper(root.left, cur+[str(root.left.val)])
        if root.right:
            self.helper(root.right, cur+[str(root.right.val)])

    def binaryTreePaths(self, root: TreeNode):
        if not root:
            return []
        self.helper(root, [str(root.val)])
        return ['->'.join(li) for li in self.res]


if __name__ == '__main__':
    pre = [1, 2, 5, 3]
    in_order = [2, 5, 1, 3]
    root = reConstructBinaryTree(pre, in_order)
    p = PrintTree()
    p.pre_order(root)
    p.print_tree()
    s = Solution()
    print(s.binaryTreePaths(root))


