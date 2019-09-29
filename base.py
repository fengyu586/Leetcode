# -*- coding: utf-8 -*-
# @Author  : Jing
# @FileName: base.py
# @IDE: PyCharm


class TreeNode:
    def __init__(self, val, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


def reConstructBinaryTree(pre, tin):
    """根据先序遍历序列和中序遍历序列构建二叉树"""
    if len(pre) == 0 or len(tin) == 0:
        return None
    if len(pre) == 1:
        return TreeNode(pre[0])
    else:
        flag = TreeNode(pre[0])
        index = tin.index(pre[0])
        flag.left = reConstructBinaryTree(pre[1:index+1],
                                               tin[:index])
        flag.right = reConstructBinaryTree(pre[index+1:],
                                                tin[index+1:])
    return flag


class link_node:
    def __init__(self, val, node=None):
        self.val = val
        self.next = node


def print_linked_list(head):
    while head:
        print(head.val)
        head = head.next
