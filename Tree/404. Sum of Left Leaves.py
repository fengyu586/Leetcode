# -*- coding: utf-8 -*-
# @Author  : Jing
# @FileName: 404. Sum of Left Leaves.py
# @IDE: PyCharm
# https://leetcode.com/problems/sum-of-left-leaves/
from base import TreeNode, PrintTree, reConstructBinaryTree


class Solution:
    def helper(self, root):
        if not root:
            return 0
        if root.left and not root.left.right and not root.left.left:
            return root.left.val + self.sumOfLeftLeaves(root.right)
        return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)

    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        res = self.helper(root)
        return res


if __name__ == '__main__':
    pre_order = [1, 2, 3, 4, 5]
    in_order = [1, 2, 4, 3, 5]
    root = reConstructBinaryTree(pre_order, in_order)
    p = PrintTree()
    p.pre_order(root)
    p.print_tree()
    s = Solution()
    print(s.sumOfLeftLeaves(root))
