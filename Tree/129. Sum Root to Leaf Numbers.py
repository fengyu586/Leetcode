# -*- coding: utf-8 -*-
# @Author  : Jing
# @FileName: 129. Sum Root to Leaf Numbers.py
# @IDE: PyCharm
# https://leetcode.com/problems/sum-root-to-leaf-numbers/
from base import TreeNode, reConstructBinaryTree, PrintTree


class Solution:
    def helper(self, root, cur):
        if not root:
            return 0
        if not root.left and not root.right:
            return int(''.join(cur+[str(root.val)]))
        left = self.helper(root.left, cur+[str(root.val)])
        right = self.helper(root.right, cur+[str(root.val)])
        return left + right

    def sumNumbers(self, root: TreeNode) -> int:
        return self.helper(root, [])


if __name__ == '__main__':
    pre_order = [4, 9, 5, 1, 0]
    in_order = [5, 9, 1, 4, 0]
    root = reConstructBinaryTree(pre_order, in_order)
    p = PrintTree()
    p.pre_order(root)
    p.print_tree()
    s = Solution()
    print(s.sumNumbers(root))



