# -*- coding: utf-8 -*-
# @Author  : Jing
# @FileName: 68.树中两个节点的最低公共祖先.py
# @IDE: PyCharm
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/     easy
# Solution 1: recursively   O(n)Time    O(n)Space
# Solution 2: iteratively   O(n)Time    O(1)Space
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
# Solution 3: recursively   O(n)Time    O(n)Space
# Solution 4: iteratively   O(n)Time    O(1)Space
from base import TreeNode, reConstructBinaryTree, PrintTree


class Solution:
    def __init__(self):
        self.res = None

    def helper(self, root, p, q):
        if not root:
            return 0
        left = self.helper(root.left, p, q)
        right = self.helper(root.right, p, q)
        if root.val == p.val or root.val == q.val:
            mid = 1
        else:
            mid = 0
        if mid + right + left >= 2:
            self.res = root
        return mid or right or left

    def lowestCommonAncestor1(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode'):
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor1(root.right, p, q)
        elif p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor1(root.left, p, q)
        else:
            return root

    def lowestCommonAncestor2(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode'):
        node = root
        while node:
            if p.val < node.val and q.val < node.val:
                node = node.left
            elif p.val > node.val and q.val > node.val:
                node = node.right
            else:
                return node
        return None

    def lowestCommonAncestor3(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode'):
        self.helper(root, p, q)
        return self.res

    def lowestCommonAncestor4(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode'):
        stack, tmp_set, parents = [root], set(), {root: None}
        while p not in parents or q not in parents:
            root = stack.pop()
            if root.left:
                parents[root.left] = root
                stack.append(root.left)
            if root.right:
                parents[root.right] = root
                stack.append(root.right)
        while q:
            tmp_set.add(q)
            q = parents[q]
        while p not in tmp_set:
            p = parents[p]
        return p


if __name__ == '__main__':
    pre_order = [6, 2, 0, 4, 3, 5, 8, 7, 9]
    in_order = [0, 2, 3, 4, 5, 6, 7, 8, 9]
    root = reConstructBinaryTree(pre_order, in_order)
    P = PrintTree()
    P.pre_order(root)
    P.print_tree()
