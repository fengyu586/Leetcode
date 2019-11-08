# -*- coding: utf-8 -*-
# @Author  : Jing
# @FileName: 617. Merge Two Binary Trees.py
# @IDE: PyCharm
# https://leetcode.com/problems/merge-two-binary-trees/
# Solution 1: iteratively   O(n)Time O(n)Space
# Solution 2: recursively   O(n)Time O(n)Space
from base import reConstructBinaryTree, PrintTree


class Solution:
    def mergeTrees1(self, t1, t2):
        if not t1:
            return t2
        stack = [(t1, t2)]
        while stack:
            n1, n2 = stack.pop()
            if not n2:
                continue
            n1.val += n2.val
            if not n1.left:
                n1.left = n2.left
            else:
                stack.append((n1.left, n2.left))
            if not n1.right:
                n1.right = n2.right
            else:
                stack.append((n1.right, n2.right))
        return t1

    def mergeTrees2(self, t1, t2):
        if not t1:
            return t2
        elif t2:
            t1.left = self.mergeTrees2(t1.left, t2.left)
            t1.right = self.mergeTrees2(t1.right, t2.right)
            t1.val += t2.val
        return t1


if __name__ == '__main__':
    preOrder1 = [1, 3, 5, 2]
    inOrder1 = [5, 3, 1, 2]
    preOrder2 = [2, 1, 4, 3, 7]
    inOrder2 = [1, 4, 2, 3, 7]
    root1 = reConstructBinaryTree(preOrder1, inOrder1)
    root2 = reConstructBinaryTree(preOrder2, inOrder2)
    p = PrintTree()
    p.pre_order(root1)
    p.print_tree()
    p.pre_order(root2)
    p.print_tree()
    s = Solution()
    root = s.mergeTrees1(root1, root2)
    p.pre_order(root)
    p.print_tree()

