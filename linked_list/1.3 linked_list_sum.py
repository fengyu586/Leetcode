#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""====================================
# @Time    : 2019/7/25 22:49
# @Author  : Jing
# @FileName: 1.3 linked_list_sum.py
# @IDE: PyCharm
======================================="""
##########################################
# 给定两个单链表，链表的每个结点代表一位数，
# 计算两个数的和。例如：输入链表（3一＞
# 1一＞5 ）和链表（5一＞9一＞2），
# 输出： 8->0->8 ， 即513+295 =8 08 ，
# 注意个位数在链表头。
# ########################################

class LNode:
    def __init__(self, x=None):
        self.data = x
        self.next = None


####################### 1、整数相加法 ###################
def add1(h1, h2):
    if h1 is None or h1.next is None:
        return h2
    if h2 is None or h2.next is None:
        return h1
    c = 0           # 用于记录进位
    sums = 0        # 用来记录两个结点相加的值
    p1 = h1.next    # 用来遍历h1
    p2 = h2.next    # 用来遍历h2
    tmp = None      # 用来指向新创建的存储相加和的结点
    result_head = LNode()       # 相加后链表头结点
    result_head.next = None
    p = result_head             # 用来指向链表result_head最后一个结点
    while p1 is not None and p2 is not None:
        tmp = LNode()
        tmp.next = None
        sums = p1.data+p2.data+c
        tmp.data = sums%10
        c = sums//10
        p.next = tmp
        p = p.next
        p1 = p1.next
        p2 = p2.next
    # 链表h2比h1长，接下来只需要考虑h2剩余结点的值
    if p1 is None:
        while p2 is not None:
            tmp = LNode()
            sums = p2.data+c
            tmp.data = sums%10
            c = sums//10
            p.next = tmp
            p = p.next
            p2 = p2.next
    # 链表h1比h2长，接下来只需要考虑h1剩余结点的值
    if p2 is None:
        while p1 is not None:
            tmp = LNode()
            sums = p1.data+c
            tmp.data = sums%10
            c = sums // 10
            p.next = tmp
            p = p.next
            p1 = p1.next
    # 如果计算完成后还有进位，则增加新的结点
    if c != 0:
        tmp = LNode()
        tmp.next = None
        tmp.data = c
        p.next = tmp
    return result_head


if __name__ == '__main__':
    i = 1
    head1 = LNode()
    head1.next = None
    head2 = LNode()
    head2.next = None
    tmp = None
    cur = head1
    add_Result = None
    # 构造第一个链表
    while i < 7:
        tmp = LNode()
        tmp.data = i+2
        tmp.next = None
        cur.next = tmp
        cur = cur.next
        i += 1
    current = head2
    # 构造第二个链表
    i = 9
    while i > 4:
        tmp = LNode()
        tmp.data = i
        tmp.next = None
        current.next = tmp
        current = current.next
        i -= 1
    print("head1: ")
    cur = head1.next
    while cur is not None:
        print(cur.data)
        cur = cur.next
    print("head2: ")
    cur = head2.next
    while cur is not None:
        print(cur.data)
        cur = cur.next
    add_Result = add1(head1, head2)
    print("相加后：")
    cur = add_Result.next
    while cur is not None:
        print(cur.data)
        cur = cur.next





