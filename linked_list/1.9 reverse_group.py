#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""====================================
# @Time    : 2019/7/28 21:41
# @Author  : Jing
# @FileName: 1.9 reverse_group.py
# @IDE: PyCharm
======================================="""
##########################################
# 题目描述：
# K 链表翻转是指把每K个相邻的结点看成一组进行翻转，
# 如果剩余结点不足K个，则保持不变。假设给定链表
# 1一>2一>3一>4一>5一>6一＞7 和一个数K,如果K的值为2,
# 那么翻转后的链表为2->l一＞4->3->6一＞5一＞70
# 如果K的值为3，那么翻转后的链表为：
# 3一＞2一>1->6一＞5->4->7 。
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


# 对不带结点的单链表翻转
def reverse(head):
    if head is None or head.next is None:
        return head
    pre = head              # 前驱结点
    cur = head.next         # 当前结点
    next = cur.next         # 后继结点
    pre.next = None
    # 使当前遍历到的结点cur指向其前驱结点
    while cur is not None:
        next = cur.next
        cur.next = pre
        pre = cur
        cur = cur.next
        cur = next
    return pre


# 对链表K翻转
def reverse_k(head, k):
    """一组一组翻转"""
    if head is None or head.next is None or k < 2:
        return
    i = 1
    pre = head
    begin = head.next
    end = None
    p_next = None
    while begin is not None:
        end = begin
        while i < k:
            if end.next is not None:
                end = end.next
            else:
                return
            i += 1
        p_next = end.next
        end.next = None
        pre.next = reverse(begin)
        begin.next = p_next
        pre = begin
        begin = p_next
        i = 1


if __name__ == '__main__':
    head = construct_list()
    print("顺序输出：")
    print_list(head)
    reverse_k(head, 3)
    print("逆序输出：")
    print_list(head)

