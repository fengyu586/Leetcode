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


def construct_list():
    """构造链表"""
    i = 1
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











