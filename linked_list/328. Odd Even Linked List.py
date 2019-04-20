#!/usr/bin/python3.6
# -*- coding:utf-8 -*-
# https://leetcode.com/problems/odd-even-linked-list/


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not(head):
            return None
        odd = head
        even = head.next
        evenHead = even
        while even and even.next:
            odd.next = odd.next.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = evenHead
        return head


def ListToListNode(li):
    res = tmp = ListNode(0)
    for i in li:
        tmp.next = ListNode(i)
        tmp = tmp.next
    return res.next


def ListNodeToList(L):
    tmp = []
    while L:
        tmp += [L.val]
        L = L.next
    return tmp


def main():
    l1 = [1, 2, 3, 4, 5]
    l1 = ListToListNode(l1)
    s = Solution()
    res = s.oddEvenList(l1)
    print(ListNodeToList(res))


if __name__ == '__main__':
    main()
