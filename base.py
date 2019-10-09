# -*- coding: utf-8 -*-
# @Author  : Jing
# @FileName: base.py
# @IDE: PyCharm


pre_order_res, in_order_res, post_order_res = [], [], []
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


def pre_order(root):
    if not root:
        return None
    pre_order_res.append(root.val)
    if root.left:
        pre_order(root.left)
    if root.right:
        pre_order(root.right)


def in_order(root):
    if not root:
        return None
    if root.left:
        in_order(root.left)
    in_order_res.append(root.val)
    if root.right:
        in_order(root.right)

def post_order(root):
    if not root:
        return None
    if root.left:
        post_order(root.left)
    if root.right:
        post_order(root.right)
    post_order_res.append(root.val)


class link_node:
    def __init__(self, val, node=None):
        self.val = val
        self.next = node


def print_linked_list(head):
    if not head:
        return head
    res = []
    while head:
        res.append(head.val)
        head = head.next
    print(res)

if __name__ == '__main__':
    preOrder = [10, 5, 4, 7, 12]
    inOrder = [4, 5, 7, 10, 12]
    flag = reConstructBinaryTree(preOrder, inOrder)
    pre_order(flag)
    in_order(flag)
    post_order(flag)
    print(pre_order_res)
    print(in_order_res)
    print(post_order_res)

