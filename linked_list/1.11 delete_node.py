#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""====================================
# @Time    : 2019/7/28 22:20
# @Author  : Jing
# @FileName: 1.11 delete_node.py
# @IDE: PyCharm
======================================="""
##########################################
# 题目描述：
# 假设给定链表1一＞2一>3一>4一>5一>6一>7中
# 指向第5个元素的指针，要求把结点5删掉，删
# 除后链表变为1一>2一>3一＞4一>6一>7。
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
    p = None
    while i < 8:
        tmp = LNode()
        tmp.data = i
        cur.next = tmp
        cur = tmp
        if i == 5:
            p = tmp
        i += 1
    return p, head


def print_list(head):
    cur = head.next
    while cur is not None:
        print(cur.data)
        cur = cur.next


def remove_node(p):
    # 如果结点为空，或结点p无后继结点则无法删除
    if p is None or p.next is None:
        return False
    p.data = p.next.data
    tmp = p.next
    p.next = tmp.next
    return True


if __name__ == '__main__':
    p, head= construct_list()
    print("删除结点"+str(p.data)+"前链表：")
    print_list(head)
    result = remove_node(p)
    if result:
        print("删除该结点后链表：")
        print_list(head)


