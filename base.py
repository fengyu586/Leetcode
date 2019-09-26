# -*- coding: utf-8 -*-
# @Author  : Jing
# @FileName: base.py
# @IDE: PyCharm


class Tree_node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class link_node:
    def __init__(self, val, node=None):
        self.val = val
        self.next = node


def print_linked_list(head):
    while head:
        print(head.val)
        head = head.next
