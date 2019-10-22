# -*- coding: utf-8 -*-
# @Author  : Jing
# @FileName: 反转链表.py
# @IDE: PyCharm
# https://www.nowcoder.com/practice/75e878df47f24fdc9dc3e400ec6058ca?tpId=13&tqId=11168&tPage=1&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking


class ListNode:
    def __init__(self, val, node=None):
        self.val = val
        self.next = node

class Solution:
    # 返回ListNode
    def ReverseList(self, Head):
        if Head is None or Head.next is None:
            return Head
        cur = Head.next
        nxt = cur.next
        cur.next = None
        pre = cur
        while nxt:
            cur = nxt
            nxt = nxt.next
            cur.nxt = pre
            pre = cur
        Head.next = cur
        return Head

    def print_node(self, Head):
        res = []
        while Head:
            res.append(Head.val)
            Head = Head.next
        return res

head = ListNode(0, None)
phead = head
for i in range(1, 6):
    node = ListNode(i)
    phead.next = node
    phead = phead.next
s = Solution()
head = s.ReverseList(head)
print(s.print_node(head))

