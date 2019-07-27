#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""====================================
# @Time    : 2019/7/27 22:30
# @Author  : Jing
# @FileName: 1.8  turn_adjacent _elements.py
# @IDE: PyCharm
======================================="""
##########################################
# 题目描述：
# 把链表相邻元素翻转，例如给定链表为
# 1-＞2一＞3一>4一＞5->6一＞7 ，则翻转后的链
# 表变为2一＞ 1 一＞4一＞3一＞6一＞5一＞7。
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
    while i < 8:
        tmp = LNode()
        tmp.data = i
        tmp.next = None
        cur.next = tmp
        cur = tmp
        i += 1
    return head


def print_list(head):
    cur = head.next
    while cur is not None:
        print(cur.data)
        cur = cur.next


####################### 1、交换值法 ###################
def reverse0(head):
    if head is None or head.next is None:
        return head
    cur = head.next
    next = cur.next
    while next is not None:
        cur.data, next.data = next.data, cur.data
        cur = next.next
        next = cur.next


####################### 2、就地逆序法 ###################
def reverse1(head):
    if head is None or head.next is None:
        return head
    pre, cur, next = head, head.next, None
    while cur is not None and cur.next is not None:
        next = cur.next.next
        pre.next = cur.next
        cur.next.next = cur
        cur.next = next
        pre = cur
        cur = next


if __name__ == '__main__':
    head = construct_list()
    print("翻转前：")
    print_list(head)
    reverse0(head)
    # reverse1(head)
    print("翻转后：")
    print_list(head)




