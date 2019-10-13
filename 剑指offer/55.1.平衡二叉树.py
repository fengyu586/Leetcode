# -*- coding: utf-8 -*-
# @Author  : Jing
# @FileName: 55.1.平衡二叉树.py
# @IDE: PyCharm
# Solution: 暴力法

def reConstructBinaryTree(pre, tin):
    """根据先序遍历序列和中序遍历序列构建二叉树"""
    if len(pre) == 0 or len(tin) == 0:
        return None
    if len(pre) == 1:
        return TreeNode(pre[0])
    else:
        flag = TreeNode(pre[0])
        index = tin.index(pre[0])
        flag.left = reConstructBinaryTree(pre[1:index + 1],
                                          tin[:index])
        flag.right = reConstructBinaryTree(pre[index + 1:],
                                           tin[index + 1:])
    return flag


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.left, self.right = 0, 0

    def Balance(self, root):
        if not root:
            return 0
        left = self.Balance(root.left)
        right = self.Balance(root.right)
        return 1+max(left, right)

    def IsBalanced(self, root):
        if not root:
            return True
        if self.IsBalanced(root.left) and self.IsBalanced(root.right):
            self.left = self.Balance(root.left)
            self.right = self.Balance(root.right)
            diff = self.left-self.right
            if abs(diff) > 1:
                return False
        return True


if __name__ == '__main__':
    preOrder = [4, 2, 1, 3, 6, 5, 7]
    inOrder = [1, 2, 3, 4, 5, 6, 7]
    flag = reConstructBinaryTree(preOrder, inOrder)
    s = Solution()
    print(s.IsBalance(flag))


