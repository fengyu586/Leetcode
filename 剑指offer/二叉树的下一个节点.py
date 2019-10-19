# -*- coding: utf-8 -*-
# @Author  : Jing
# @FileName: 二叉树的下一个节点.py
# @IDE: PyCharm


class TreeLinkNode:
    def __init__(self, x):
            self.val = x
            self.left = None
            self.right = None
            self.next = None


class Solution:
    def GetNext(self, pNode):
        # write code here
        if not pNode:
            return pNode
        # 若该结点为根节点
        if not pNode.next:
            if pNode.right:
                node = pNode.right
                while node and node.left:
                    node = node.left
            else:
                node = pNode.next
            return node

        # 该节点为父节点的左子节点
        elif pNode.next.left and pNode.next.left.val == pNode.val:
            if pNode.right:
                node = pNode.right
                while node and node.left:
                    node = node.left
            else:
                node = pNode.next
            return node
        # 若该节点为父结点的右子节点
        elif pNode.next.right and pNode.next.right.val == pNode.val:
            if pNode.right:
                node = pNode.right
                while node and node.left:
                    node = node.left
            else:
                node = pNode.next
                while node and node.next and node.next.right and node.next.right.val == node.val:
                    node = node.next
                node = node.next
            return node


