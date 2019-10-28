# -*- coding: utf-8 -*-
# @Author  : Jing
# @FileName: 107. Binary Tree Level Order Traversal II.py
# @IDE: PyCharm
# https://leetcode.com/problems/binary-tree-level-order-traversal-ii/
# Solution 1: bfs+queue O(NL)Time O(N)Space
# Solution 2: dfs+stack O(NL)Time O(N)Space
# Solution 3: dfs recursively O(NL)Time O(N)Space
from base import TreeNode, reConstructBinaryTree


class Solution:
    def levelOrderBottom1(self, root:TreeNode):
        if not root:
            return []
        cur, res = [], []
        nodes = [root]
        leaves_num = 1
        next_level = 0
        while nodes:
            node = nodes.pop(0)
            cur.append(node.val)
            if node.left:
                nodes.append(node.left)
                next_level += 1
            if node.right:
                nodes.append(node.right)
                next_level += 1
            leaves_num -= 1
            if leaves_num == 0:
                res.insert(0, cur)
                cur = []
                leaves_num = next_level
                next_level = 0
        return res

    def levelOrderBottom2(self, root):
        stack = [(root, 0)]
        res = []
        while stack:
            node, level = stack.pop()
            if node:
                if len(res) < level+1:
                    res.insert(0, [])
                res[-(level+1)].append(node.val)
                stack.append((node.right, level+1))
                stack.append((node.left, level+1))
        return res

    def dfs3(self, root, level, res):
        if root:
            if len(res) < level+1:
                res.insert(0, [])
            res[-(level+1)].append(root.val)
            self.dfs3(root.left, level+1, res)
            self.dfs3(root.right, level+1, res)

    def levelOrderBottom3(self, root):
        res = []
        self.dfs3(root, 0, res)
        return res


if __name__ == '__main__':
    preOrder = [3, 9, 20, 15, 7]
    inOrder = [9, 3, 15, 20, 7]
    flag = reConstructBinaryTree(preOrder, inOrder)
    s = Solution()
    print(s.levelOrderBottom1(flag))


