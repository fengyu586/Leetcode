#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""====================================
# @Time    : 2019/7/25 22:13
# @Author  : Jing
# @FileName: 1.2 remove_duplicate.py
# @IDE: PyCharm
======================================="""
##########################################
# 给定一个没有排序的链表，去掉其重复项，
# 并保留原顺序，例如链表1 ->3 -> 1 一＞5一＞5 ->7,
# 去掉重复项后变为l 一＞3 一＞ 5 ->7 。
# ########################################

class LNode:
    def _new_(self, x):
        self.data = x
        self.next = None


####################### 1、顺序删除 ###################
def remove_dup1(head):
    if head is None or head.next is None:
        return
    outer_cur = head.next       # 用于外层循环，指向链表的第一个结点
    inner_cur = None            # 用于内层循环，遍历outer_cur后面的结点
    inner_pre = None            # inner_cur的前驱结点
    while outer_cur is not None:
        inner_cur = outer_cur.next
        inner_pre = outer_cur
        while inner_cur is not None:
            # 找到重复结点并删除
            if outer_cur.data == inner_cur.data:
                inner_pre.next =inner_cur.next
                inner_cur = inner_cur.next
            else:
                inner_pre = inner_cur
                inner_cur = inner_cur.next
        outer_cur = outer_cur.next


####################### 2、递归法 ###################
def remove_dup_recursion(head):
    if head.next is None:
        return head
    pointer = None
    cur = head
    # 对以head.next为首的子链表删除重复的结点
    head.next = remove_dup_recursion(head.next)
    pointer = head.next
    # 找出以head.next为首的子链表中与head结点相同的结点并删除
    while pointer is not None:
        if head.data == pointer.data:
            cur.next = pointer.next
            pointer = cur.next
        else:
            pointer = pointer.next
            cur = cur.next
    return head


def remove_dup2(head):
    if head is None:
        return
    head.next = remove_dup_recursion(head.next)

if __name__ == '__main__':
    i = 1
    head = LNode()
    head.next = None
    tmp = None
    cur = head
    while i < 7:
        tmp = LNode()
        if  i%2 == 0:
            tmp.data = i+1
        elif i%3 == 0:
            tmp.data = i-2
        else:
            tmp.data = i
        tmp.next = None
        cur.next = tmp
        cur = cur.next
        i += 1
    print("删除重复结点前：")
    current = head.next
    while current is not None:
        print(current.data)
        current = current.next
    # remove_dup1(head)
    remove_dup2(head)
    print("删除重复结点后：")
    cur = head.next
    while cur is not None:
        print(cur.data)
        cur = cur.next







