# -*- coding: utf-8 -*-
# @Author  : Jing
# @FileName: 113. Path Sum II.py
# @IDE: PyCharm
# https://leetcode.com/problems/path-sum-ii/
from base import reConstructBinaryTree


class Solution:
    def hasPath(self, root, cur, sum, path, res):
        if not root.left and not root.right:
            if cur == sum:
                res.append(path)
            return
        if root.left:
            self.hasPath(root.left, cur + root.left.val, sum, path + [root.left.val], res)
        if root.right:
            self.hasPath(root.right, cur + root.right.val, sum, path + [root.right.val], res)
        return

    def pathSum(self, root, sum):
        if not root:
            return []
        res, path = [], [root.val]
        cur = root.val
        self.hasPath(root, cur, sum, path, res)
        return res


if __name__ == '__main__':
    preOrder = [5, 4, 11, 7, 2, 8, 13, 4, 5, 1]
    inOrder = [7, 11, 2, 4, 5, 13, 8, 5, 4, 1]
    flag = reConstructBinaryTree(preOrder, inOrder)
    target = 22
    s = Solution()
    print(s.pathSum(flag, target))