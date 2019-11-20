# -*- coding: utf-8 -*-
# @Author  : Jing
# @FileName: 102. Binary Tree Level Order Traversal.py
# @IDE: PyCharm
# https://leetcode.com/problems/binary-tree-level-order-traversal/
# Solution 1: DFS
# Solution 2: iteratively
from base import TreeNode, reConstructBinaryTree, PrintTree


class Solution:
    def helper(self, root, level, res):
        if not root:
            return None
        if len(res) < level + 1:
            res.append([])
        res[level].append(root.val)
        self.helper(root.left, level+1, res)
        self.helper(root.right, level+1, res)

    def levelOrder1(self, root: TreeNode):
        res, level = [], 0
        self.helper(root, level, res)
        return res

    def levelOrder2(self, root: TreeNode):
        res = []
        if not root:
            return []
        stack, nodes_num, next_nodes, cur = [root], 1, 0, []
        while stack:
            root = stack.pop(0)
            cur.append(root.val)
            if root.left:
                next_nodes += 1
                stack.append(root.left)
            if root.right:
                next_nodes += 1
                stack.append(root.right)
            nodes_num -= 1
            if nodes_num == 0:
                res.append(cur)
                cur = []
                nodes_num = next_nodes
                next_nodes = 0
        return res


if __name__ == '__main__':
    pre_order, in_order = [3, 9, 20, 15, 7], [9, 3, 15, 20, 7]
    root = reConstructBinaryTree(pre_order, in_order)
    s = Solution()
    p = PrintTree()
    p.pre_order(root)
    p.print_tree()
    print(s.levelOrder1(root))