#!/usr/bin/python3.6
# -*- coding:utf-8 -*-
# https://leetcode.com/problems/rotate-list/


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        length = 1
        cur = head
        if not(cur):
            return cur
        while cur.next:
            length += 1
            cur = cur.next
        val = k % length
        if val == 0:
            return head
        cur.next = head
        val = length - val
        while val > 1:
            head = head.next
            val -= 1
        new_head = head.next
        head.next = None
        return new_head


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
    n = 2
    l1 = ListToListNode(l1)
    s = Solution()
    res = s.rotateRight(l1, n)
    print(ListNodeToList(res))


if __name__ == '__main__':
    main()



