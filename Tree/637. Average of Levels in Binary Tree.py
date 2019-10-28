# -*- coding: utf-8 -*-
# @Author  : Jing
# @FileName: 637. Average of Levels in Binary Tree.py
# @IDE: PyCharm
# https://leetcode.com/problems/average-of-levels-in-binary-tree/
# Solution 1: dfs O(n)Time O(h)Space
# Solution 2: bfs O(n)Time O(h)Space
from base import TreeNode, reConstructBinaryTree


class Solution:
    def dfs(self, root, level, res):
        if root:
            if len(res) < level+1:
                res.append([0, 0])
            res[level][0] += root.val
            res[level][1] += 1
            self.dfs(root.right, level+1, res)
            self.dfs(root.left, level+1, res)

    def averageOfLevels1(self, root: TreeNode):
        if not root:
            return []
        res = []
        self.dfs(root, 0, res)
        return [li[0]/li[1] for li in res]

    def averageOfLevels2(self, root:TreeNode):
        if not root:
            return []
        res, nodes = [], [root]
        cur_level, count = 1, 1
        cur_sum, next_level = 0, 0
        while nodes:
            node = nodes.pop(0)
            cur_sum += node.val
            if node.left:
                nodes.append(node.left)
                next_level += 1
            if node.right:
                nodes.append(node.right)
                next_level += 1
            count -= 1
            if count == 0:
                res.append(cur_sum/cur_level)
                count, cur_level = next_level, next_level
                cur_sum, next_level = 0, 0
        return res


if __name__ == '__main__':
    preOrder = [3, 9, 20, 15, 7]
    inOrder = [9, 3, 15, 20, 7]
    flag = reConstructBinaryTree(preOrder, inOrder)
    s = Solution()
    print(s.averageOfLevels2(flag))

