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


class PrintTree(object):
    def __init__(self):
        self.res = []

    def pre_order(self, root):
        if not root:
            return None
        self.res.append(root.val)
        if root.left:
            self.pre_order(root.left)
        if root.right:
            self.pre_order(root.right)

    def in_order(self, root):
        if not root:
            return None
        if root.left:
            self.in_order(root.left)
        self.res.append(root.val)
        if root.right:
            self.in_order(root.right)

    def post_order(self, root):
        if not root:
            return None
        if root.left:
            self.post_order(root.left)
        if root.right:
            self.post_order(root.right)
        self.res.append(root.val)

    def print_tree(self):
        print(self.res)
        self.res = []


class ListNode:
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

def contruct_linked_list(nums):
    if not nums:
        return None
    header = ListNode(nums[0])
    cur = header
    for num in nums[1:]:
        node = ListNode(num)
        cur.next = node
        cur = cur.next
    return header


if __name__ == '__main__':
    preOrder = [10, 5, 4, 7, 12]
    inOrder = [4, 5, 7, 10, 12]
    flag = reConstructBinaryTree(preOrder, inOrder)
    p = PrintTree()
    p.pre_order(flag)
    p.print_tree()
    p.in_order(flag)
    p.print_tree()
    p.post_order(flag)
    p.print_tree()

