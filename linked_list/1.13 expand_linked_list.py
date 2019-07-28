#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""====================================
# @Time    : 2019/7/28 22:59
# @Author  : Jing
# @FileName: 1.13 expand_linked_list.py
# @IDE: PyCharm
======================================="""
##########################################
# 题目描述：
# 给定一个有序链表，其中每个结点也表示一个有序链表，
# 结点包含两个类型的指针：
# （1）指向主链表中下一个结点的指针（在下面的代码中称为“正确”指针）
# （2）指向此结点头的链表（在下面的代码中称之为“down＂指针〉。
# ########################################

class Node:
    def __init__(self, data=None):
        self.data = data
        self.right = None
        self.down = None


class merge_list:
    def __init__(self):
        self.head = None

        # 用来合并两个有序的链表
    def merge(self, a, b):
        # 如果有其中一个链表为空，直接返回另外一个链表
        if a is None:
            return b
        if b is None:
            return a

        # 把两个链表头中较小的结点赋值给result
        if a.data < b.data:
            result = a
            result.down = self.merge(a.down, b)
        else:
            result = b
            result.down = self.merge(a, b.down)
        return result

    # 把链表扁平化处理
    def flatten(self, root):
        if root is None or root.right is None:
            return root

        # 递归处理root.right链表
        root.right = self.flatten(root.right)

        # 把root结点对应的链表与右边的链表合并
        root = self.merge(root, root.right)
        return root

    # 把data插入到链表头
    def insert(self, head_ref, data):
        new_node = Node(data)
        new_node.down = head_ref
        head_ref = new_node

        # 返回新的表头结点
        return head_ref

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.down


if __name__ == '__main__':
    L = merge_list()

    # 构造链表
    L.head = L.insert(L.head, 31)
    L.head = L.insert(L.head, 8)
    L.head = L.insert(L.head, 6)
    L.head = L.insert(L.head, 3)
    L.head.right = L.insert(L.head.right, 21)
    L.head.right = L.insert(L.head.right, 11)
    L.head.right.right = L.insert(L.head.right.right, 50)
    L.head.right.right = L.insert(L.head.right.right, 22)
    L.head.right.right = L.insert(L.head.right.right, 15)
    L.head.right.right.right = L.insert(L.head.right.right.right, 55)
    L.head.right.right.right = L.insert(L.head.right.right.right, 40)
    L.head.right.right.right = L.insert(L.head.right.right.right, 39)
    L.head.right.right.right = L.insert(L.head.right.right.right, 30)

    # 扁平化链表
    L.head = L.flatten(L.head)
    L.print_list()




