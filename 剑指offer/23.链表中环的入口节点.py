# -*- coding: utf-8 -*-
# @Author  : Jing
# @FileName: 23.链表中环的入口节点.py
# @IDE: PyCharm


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isLoop(self, pHead):
        if pHead and pHead.next and pHead.next.next:
            cur, nxt = pHead, pHead.next.next
            while nxt and nxt.next and nxt.next.next:
                if cur.val == nxt.val:
                    return True
                cur = cur.next
                nxt = nxt.next.next
        return False

    def getNumberOfnodes(self, pHead):
        if pHead and pHead.next and pHead.next.next:
            cur, nxt = pHead, pHead.next.next
            while nxt and nxt.next and nxt.next.next:
                if cur.val == nxt.val:
                    break
                cur = cur.next
                nxt = nxt.next.next
            count = 1
            nxt = nxt.next
            while nxt.val != cur.val:
                count += 1
                nxt = nxt.next
            return count

    def EntryNodeOfLoop(self, pHead):
        # write code here
        if not pHead:
            return None
        flag = self.isLoop(pHead)
        if flag:
            number = self.getNumberOfnodes(pHead)
            cur, nxt = pHead, pHead
            while number > 0:
                nxt = nxt.next
                number -= 1
            while nxt.val != cur.val:
                cur = cur.next
                nxt = nxt.next
            return cur
        else:
            return None
