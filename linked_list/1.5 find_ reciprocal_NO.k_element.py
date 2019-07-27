#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""====================================
# @Time    : 2019/7/27 19:38
# @Author  : Jing
# @FileName: 1.5 find_ reciprocal_NO.k_element.py
# @IDE: PyCharm
======================================="""
##########################################
# 题目描述：
# 找出单链表中的倒数第k个元素，例如给定单链表：
# 1->2一＞ 3 一＞4 一＞5 一＞6 一＞7 ，则单链表
# 的倒数第k=3个元素为5 。
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


####################### 1、顺序遍历法 ###################
def find_last_k0(head, k):
    sums = 0
    tmp = head.next
    while tmp is not None:
        sums += 1
        tmp = tmp.next
    n = sums-k
    cur = head.next
    while n != 0:
        n -= 1
        cur = cur.next
    return cur


####################### 2、快慢指针法 ###################
def find_last_k1(head, k):
    fast, low = head.next, head.next
    while fast is not None and k != 0:
        k -= 1
        fast = fast.next
    if k != 0:
        return None
    while fast is not None:
        low = low.next
        fast = fast.next
    return low




if __name__ == '__main__':
    index = 3
    head = construct_list()
    print("链表：")
    print_list(head)
    # res = find_last_k0(head, index)
    res = find_last_k1(head, index)
    print("链表倒数第{}个元素为：{}".format(index, res.data))




