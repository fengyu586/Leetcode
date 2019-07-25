#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""====================================
# @Time    : 2019/7/24 20:51
# @Author  : Jing
# @FileName: 1.1 reverse_linked_list.py
# @IDE: PyCharm
# @ python程序员面试算法宝典 p22
======================================="""
##########################################
# 给定一个带头结点的单链表，请将其逆序。
# 即如果单链表原来为head->1一＞2->3->4->5一＞6一＞7
# 那么逆序后变为head一＞7一＞6一＞5->4->3>2->1
# ########################################
class LNode:
    def _new_(self, x):
        self.data = x
        self.next = None


####################### 1、就地逆序 ###################
def reverse1(head):
    # 判断链表是否为空
    if head is None or head.next is None:
        return
    # pre = None      # 前驱结点
    # cur = None      # 当前结点
    # next = None     # 后继结点
    # 把链表首结点变为尾结点
    cur = head.next
    next = cur.next
    cur.next = None
    pre = cur
    cur = next
    # 使当前遍历到的结点cur指向其前驱结点
    while cur.next != None:
        next = cur.next
        cur.next = pre
        pre = cur
        # cur = cur.next
        cur = next
    # 链表最后一个结点指向倒数第二个结点
    cur.next = pre
    # 链表的头结点指向原来链表的尾结点
    head.next = cur


####################### 2、递归法 ###################
def recursive_reverse(head):
    """
    方法功能: 对不带头结点的单链表进行逆序
    输入参数：firstRef:链表头结点
    """
    # 如果链表为空或者链表中只有一个元素
    if head is None or head.next is None:
        return head
    else:
        # 反转后面的结点
        new_head = recursive_reverse(head.next)
        head.next.next = head
        head.next = None
        return new_head


def reverse2(head):
    """
    方法功能: 对带头结点的单链表进行逆序
    输入参数：head:链表头结点
    """
    if head is None:
        return
    # 获取链表第一个结点
    first_node = head.next
    # 对链表进行逆序
    new_head = recursive_reverse(first_node)
    # 头结点指向逆序后的链表的第一个结点
    head.next = new_head
    return new_head


####################### 3、插入法 ###################
def reverse3(head):
    # 判断链表是否为空
    if head is None or head.next is None:
        return
    cur = head.next.next
    head.next.next = None
    # 将遍历到的结点插入到头结点的后面
    while cur is not None:
        next = cur.next
        cur.next = head.next
        head.next = cur
        cur = next


if __name__ == '__main__':
    i = 1
    # 链表头结点
    head = LNode()
    head.next = None
    tmp = None
    cur = head
    # 构造单链表
    while i < 8:
        tmp = LNode()
        tmp.data = i
        tmp.next = None
        cur.next = tmp
        cur = cur.next
        i += 1
    print("逆序前：")
    current = head.next
    while current:
        print(current.data)
        current = current.next
    print("逆序后：")
    # reverse1(head)
    # reverse2(head)
    reverse3(head)
    cur = head.next
    while cur:
        print(cur.data)
        cur = cur.next




