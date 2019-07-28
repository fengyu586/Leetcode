#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""====================================
# @Time    : 2019/7/28 22:32
# @Author  : Jing
# @FileName: 1.12 Determine_whether_to_cross.py
# @IDE: PyCharm
======================================="""
##########################################
# 题目描述：
# 单链表相交指的是两个链表存在完全重合的部分。
# ########################################

class LNode:
    def __init__(self, x=None):
        self.data = x
        self.next = None


def construct_list0():
    """构造链表"""
    i = 1
    head = LNode()
    tmp = None
    cur = head
    p = None
    while i < 8:
        tmp = LNode()
        tmp.data = i
        cur.next = tmp
        cur = tmp
        if i == 5:
            p = tmp
        i += 1
    return p, head


def construct_list1(p):
    """构造链表"""
    i = 1
    head = LNode()
    tmp = None
    cur = head
    while i < 5:
        tmp = LNode()
        tmp.data = i
        cur.next = tmp
        cur = tmp
        i += 1
    cur.next = p
    return head


def print_list(head):
    cur = head.next
    while cur is not None:
        print(cur.data)
        cur = cur.next


####################### 1、交换值法 ###################
def is_intersect(head1, head2):
    if head1 is None or head1.next is None or \
            head2 is None or head2.next is None \
            or head1 == head2:
        return None
    temp1 = head1.next
    temp2 = head2.next
    n1, n2 = 0, 0

    # 遍历head1，找到尾结点，同时记录head1的长度
    while temp1.next is not None:
        temp1 = temp1.next
        n1 += 1

    # 遍历head2，找到尾结点，同时记录head2的长度
    while temp2.next is not None:
        temp2 = temp2.next
        n2 += 1

    # head1与head2是有相同的尾结点
    if temp1 == temp2:

        # 长链表先走|n1-n2|步
        if n1 > n2:
            head1 = head1.next
            n1 -= 1
        if n2 > n1:
            while n2 - n1 > 0:
                head2 = head2.next
                n2 -= 1

        # 两个链表同时前进，找出相同的结点
        while head1 != head2:
            head1 = head1.next
            head2 = head2.next
        return head1

    # head1与head2是没有相同的尾结点
    else:
        return None


if __name__ == '__main__':
    p, head1 = construct_list0()
    head2 = construct_list1(p)
    print("head1：")
    print_list(head1)
    print("head2：")
    print_list(head2)
    inter_node = is_intersect(head1, head2)
    if inter_node is None:
        print("这两个链表不相交：")
    else:
        print("这两个链表相交点为："+str(inter_node.data))




