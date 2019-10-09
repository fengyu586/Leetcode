# -*- coding: utf-8 -*-
# @Author  : Jing
# @FileName: 36.二叉搜索树与双向链表.py
# @IDE: PyCharm
from base import print_linked_list

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
    def ConvertNode(self, root):
        global cur
        if not root:
            return
            # 转左子树
        pCur = root
        if pCur.left:
            self.ConvertNode(pCur.left)
        pCur.left = cur
        if cur:
            cur.right = pCur
        cur = pCur
        # 转右子树
        if pCur.right:
            self.ConvertNode(pCur.right)

    def Convert(self, pRootOfTree):
        # write code here
        global cur
        self.ConvertNode(pRootOfTree)
        while cur and cur.left:
            cur = cur.left
        return cur


if __name__ == '__main__':
    preOrder = [4, 2, 1, 3, 6, 5, 7]
    inOrder = [1, 2, 3, 4, 5, 6, 7]
    flag = reConstructBinaryTree(preOrder, inOrder)
    s = Solution()
    cur = None
    head = s.Convert(flag)
    while head:
        print(head.val)
        head = head.right

