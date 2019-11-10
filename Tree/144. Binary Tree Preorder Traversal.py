# -*- coding: utf-8 -*-
# @Author  : Jing
# @FileName: 144. Binary Tree Preorder Traversal.py
# @IDE: PyCharm
# https://leetcode.com/problems/binary-tree-preorder-traversal/
# Solution 1: recursively   O(n)Time O(n)Space
# Solution 2: iteratively   O(n)Time O(n)Space


from base import reConstructBinaryTree


class Solution:
    def __init__(self):
        self.res = []

    def preorder1(self, root):
        if not root:
            return None
        self.res.append(root.val)
        if root.left:
            self.preorder1(root.left)
        if root.right:
            self.preorder1(root.right)
        return

    def preorder2(self, root):
        stack = [root, ]
        while stack:
            node = stack.pop()
            if node:
                self.res.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return self.res

    def preorderTraveral1(self, root):
        self.preorder1(root)
        return self.res

    def preorderTraveral2(self, root):
        self.preorder2(root)
        return self.res


if __name__ == '__main__':
    preOrder = [1, 2, 3]
    inOrder = [1, 3, 2]
    root = reConstructBinaryTree(preOrder, inOrder)
    s = Solution()
    print(s.preorderTraveral1(root))


