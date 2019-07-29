#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""====================================
# @Time    : 2019/7/29 17:47
# @Author  : Jing
# @FileName: 2.1.py
# @IDE: PyCharm
======================================="""
##########################################
# 题目描述：
# 实现一个栈的数据结构，使其具有以下方法：
# 压栈、弹栈、取栈顶元素、判断栈是否为空
# 以及获取栈中元素个数。
# ########################################
####################### 1、数组法 ###################
class MyStack0:
    # 模拟栈
    def __init__(self):
        self.items = []

    # 判断栈是否为空
    def is_empty(self):
        return len(self.items)==0

    # 返回栈的大小
    def size(self):
        return len(self.items)

    # 返回栈顶元素
    def top(self):
        if not self.is_empty():
            return self.items[len(self.items)-1]
        else:
            return None
     # 弹栈
    def pop(self):
        if len(self.items) > 0:
            return self.items.pop()
        else:
            print("栈已经为空")
            return None

    # 压栈
    def push(self, item):
        self.items.append(item)

####################### 2、链表法 ###################
class LNode:
    def __init__(self, x=None):
        self.data = x
        self.next = None


class MyStack1:
    def __init__(self):
        self.data = None
        self.next = None

    # 判断栈是否为空
    def empty(self):
        if self.next is None:
            return True
        else:
            return False

    # 获取栈中元素的个数
    def size(self):
        size = 0
        p = self.next
        while p is not None:
            size += 1
            p = p.next
        return size

    # 入栈
    def push(self, e):
        p = LNode()
        p.data = e
        cur = self.next
        if cur is None:
            self.next = p
        else:
            while cur.next is not None:
                cur = cur.next
            cur.next = p
        return self

    # 出栈
    def pop(self):
        tmp = self.next
        if tmp is None:
            print("栈已经为空")
            return None
        else:
            while tmp.next is not None:
                tmp = tmp.next
            return tmp

    # 取得栈顶元素
    def top(self):
        cur = self.next
        if cur is None:
            return self.next.data
        else:
            while cur.next is not None:
                cur = cur.next
            return cur.data


if __name__ == '__main__':
    s = MyStack1()
    s.push(4)
    s.push(2)
    print("栈顶元素为：", s.top())
    print("栈大小为：", s.size())
    s.pop()
    print("弹栈成功")
    s.pop()
