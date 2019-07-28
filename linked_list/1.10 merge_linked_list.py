#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""====================================
# @Time    : 2019/7/28 21:59
# @Author  : Jing
# @FileName: 1.10 merge_linked_list.py
# @IDE: PyCharm
======================================="""
##########################################
# 题目描述：
# 己知两个链表headl和head2各自有序（例如升序排列），
# 请把它们合并成一个链表，要求合并后的链表依然有序。
# ########################################

class LNode:
    def __init__(self, x=None):
        self.data = x
        self.next = None


def construct_list(start):
    """构造链表"""
    i = start
    head = LNode()
    tmp = None
    cur = head
    while i < 7:
        tmp = LNode()
        tmp.data = i
        cur.next = tmp
        cur = tmp
        i += 2
    return head


def print_list(head):
    cur = head.next
    while cur is not None:
        print(cur.data)
        cur = cur.next


def merge(head1, head2):
    if head1 is None or head1.next is None:
        return head2
    if head2 is None or head2.next is None:
        return head1
    cur1 = head1.next               # 用来遍历head1
    cur2 = head2.next               # 用来遍历head2
    head = None                     # 合并后链表的头结点
    cur = None                      # 合并后的链表在尾结点
    if cur1.data > cur2.data:
        head = head2
        cur = cur2
        cur2 = cur2.next
    else:
        head = head1
        cur = cur1
        cur1 = cur1.next

    # 每次找链表剩余结点的最小值对应的结点连接到合并后链表的尾部
    while cur1 is not None and cur2 is not None:
        if cur1.data < cur2.data:
            cur.next = cur1
            cur = cur1
            cur1 = cur1.next
        else:
            cur.next = cur2
            cur = cur2
            cur2 = cur2.next
    # 当遍历完一个链表后把另外一个链表剩余的结点链接到合并后的链表后面。
    if cur1 is not None:
        cur.next = cur1
    if cur2 is not None:
        cur.next = cur2
    return head


if __name__ == '__main__':
    head1 = construct_list(1)
    head2 = construct_list(2)
    print("head1: ")
    print_list(head1)
    print("head2: ")
    print_list(head2)
    print("合并后的链表：")
    head = merge(head1, head2)
    print_list(head)


