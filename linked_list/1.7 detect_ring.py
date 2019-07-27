#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""====================================
# @Time    : 2019/7/27 20:53
# @Author  : Jing
# @FileName: 1.7 detect_ring.py
# @IDE: PyCharm
======================================="""
##########################################
# 题目描述：
# 单链表有环指的是单链表中某个结点的next域指
# 向的是链表中在它之前的某一个结点，这样在链
# 表的尾部形成一个环形结构。如何判断单链表是
# 否有环存在？
# ########################################

class LNode:
    def __init__(self, x=None):
        self.data = x
        self.next = None


def construct_list():
    """构造链表"""
    i = 1
    head = LNode()
    cur = head
    while i < 8:
        tmp = LNode()
        tmp.data = i
        cur.next = tmp
        cur = cur.next
        i += 1
    cur.next = head.next
    return head


def is_loop(head):
    """判断是否有环"""
    if head is None or head.next is None:
        return None
    slow, fast = head.next, head.next
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return slow
    return None


def find_loop_node(head, meet_node):
    first = head.next
    second = meet_node
    while first != second:
        while second.next != meet_node:
            if first == second or first == second.next:
                return first
            second = second.next

        second = second.next
        first = first.next
    return first


if __name__ == '__main__':
    head = construct_list()
    meet_node = is_loop(head)
    if meet_node is not None:
        print("有环")
        loop_node = find_loop_node(head, meet_node)
        print("环的入口点为：{}".format(loop_node.data))
    else:
        print("无环")












