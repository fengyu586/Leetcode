# -*- coding: utf-8 -*-
# @Author  : Jing
# @FileName: 111. Minimum Depth of Binary Tree.py
# @IDE: PyCharm
# https://leetcode.com/problems/minimum-depth-of-binary-tree/
from base import reConstructBinaryTree, PrintTree


class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        left = left if left else right
        right = right if right else left
        return min(left, right) + 1


if __name__ == '__main__':
    pre, inorder = [3, 9, 20, 15, 7], [9, 3, 15, 20, 7]
    root = reConstructBinaryTree(pre, inorder)
    p = PrintTree()
    p.pre_order(root)
    p.print_tree()
    s = Solution()
    print(s.minDepth(root))