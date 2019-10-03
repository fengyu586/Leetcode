# -*- coding: utf-8 -*-
# @Author  : Jing
# @FileName: 合并排序链表.py
# @IDE: PyCharm


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        if not pHead1 or not pHead2:
            return pHead1 or pHead2
        pHead = None
        if pHead1.val < pHead2.val:
            pHead = pHead1
            pHead1 = pHead1.next
        else:
            pHead = pHead2
            pHead2 = pHead2.next
        node = pHead
        while pHead1 and pHead2:
            if pHead1.val < pHead2.val:
                node.next = pHead1
                pHead1 = pHead1.next
            else:
                node.next = pHead2
                pHead2 = pHead2.next
            node = node.next
        node.next = pHead1 if pHead1 else pHead2
        return pHead
