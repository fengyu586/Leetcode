#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""====================================
# @Time    : 2019/7/26 22:02
# @Author  : Jing
# @FileName: 1.4 resorted_linked_list.py
# @IDE: PyCharm
======================================="""
##########################################
# 题目描述：
# 给定链表Lo一＞L1 一＞L2 … Ln-1 一＞Ln ，
# 把链表重新排序为Lo >Ln一＞L1 一＞Ln-1->L2一＞ Ln-2…。
# 要求： Cl ）在原来链表的基础上进行排序，
# 即不能申请新的结点：（ 2 ）只能修改结点的next域，
# 不能修改数据域。
# ########################################
class LNode():
    def __init__(self, x=None):
        self.data = x
        self.next = None


def find_middle_node(head):
    if head is None or head.next is None:
        return head
    fast = head             # 遍历链表的时候每次向前走两步
    slow = head             # 遍历链表的时候每次向前走一步
    slow_pre = head         # 当fast到链表尾时，slow恰好指向链表的中间结点
    while fast is not None and fast.next is not None:
        slow_pre = slow
        slow = slow.next
        fast = fast.next.next           # 把链表断开成两个独立的子链表
    slow_pre.next = None
    return slow


def reverse(head):
    if head is None or head.next is None:
        return head
    pre = head          # 前驱结点
    cur = head.next          #当前结点
    next = cur.next     # 后继结点
    pre.next = None     # 使当前遍历到的结点cur指向其前驱结点
    while cur is not None:
        next = cur.next
        cur.next = pre
        pre = cur
        cur = next
    return pre


def reorder(head):
    if head is None or head.next is None:
        return

    # 前半部分链表第一个结点
    cur1 = head.next
    mid = find_middle_node(head.next)

    # 后半部分链表逆序后的第一个结点
    cur2 = reverse(mid)
    tmp = None

    # 合并两个链表
    while cur1.next is not None:
        tmp = cur1.next
        cur1.next = cur2
        cur1 = tmp
        tmp = cur2.next
        cur2.next = cur1
        cur2 = tmp
    cur1.next = cur2


if __name__ == '__main__':
    i = 1
    head = LNode()
    head.next = None
    tmp = None
    cur = head

    # 构造第一个链表
    while i < 8:
        tmp = LNode()
        tmp.data = i
        tmp.next = None
        cur.next = tmp
        cur = cur.next
        i += 1
    print("排序前：")
    current = head.next
    while current is not None:
        print(current.data)
        current = current.next
    reorder(head)
    print("排序后：")
    cur = head.next
    while cur is not None:
        print(cur.data)
        cur = cur.next








