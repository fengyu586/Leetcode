# -*- coding: utf-8 -*-
# @Author  : Jing
# @FileName: 112. Path Sum.py
# @IDE: PyCharm
# https://leetcode.com/problems/path-sum/
from base import reConstructBinaryTree


class Solution:
    def hasPathSum(self, root, sum):
        if not root:
            return False
        sum -= root.val
        if not root.left and not root.right:
            return sum == 0
        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)


if __name__ == '__main__':
    preOrder = [5, 4, 11, 7, 2, 8, 13, 4, 1]
    inOrder = [7, 11, 2, 4, 5, 13, 8, 4, 1]
    flag = reConstructBinaryTree(preOrder, inOrder)
    target = 22
    s = Solution()
    print(s.hasPathSum(flag, target))