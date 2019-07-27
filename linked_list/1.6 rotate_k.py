#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""====================================
# @Time    : 2019/7/27 20:21
# @Author  : Jing
# @FileName: 1.6 rotate_k.py
# @IDE: PyCharm
======================================="""
##########################################
# 题目描述： 给定单链表 1-＞2->3 一＞4一＞ 5->6->7'
# k=3 ，那么旋转后的单链表变为
# 5-> 6->7- > 1->2 一＞3 一＞4。
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


####################### 1、快慢指针法 ###################
def rotate_k1(head, k):
    pre, cur, next = head, head.next, head.next
    while next is not None and k != 0:
        k -= 1
        next = next.next
    if k != 0:
        return None
    while next is not None:
        cur = cur.next
        next = next.next
        pre = pre.next
    pre.next = next
    tmp = head.next
    head.next = cur
    new_cur = cur
    while new_cur.next is not None:
        new_cur = new_cur.next
    new_cur.next = tmp
    return head


if __name__ == '__main__':
    index = 3
    head = construct_list()
    print("链表：")
    print_list(head)
    # res = find_last_k0(head, index)
    res = rotate_k1(head, index)
    print("旋转后：")
    print_list(res)
















