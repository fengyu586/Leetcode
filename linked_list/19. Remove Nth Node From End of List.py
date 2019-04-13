#!/usr/bin/python3.6
# -*- coding:utf-8 -*-
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# Approach 1: Two pass algorithm
# Approach 2: 通过两个间隔为n+1的指针进行遍历


def ListNodeToList(L):
    tmp = []
    while L:
        tmp += [L.val]
        L = L.next
    return tmp


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd1(self, head, n):
        length = 0
        tmp = head
        while tmp:
            length += 1
            tmp = tmp.next
        if length == 1:
            return None
        if length == n:
            return head.next
        tmp = head
        position = 1
        while tmp:
            if position == (length-n):
                tmp.next = tmp.next.next
                return head
            else:
                position += 1
                tmp = tmp.next

    def removeNthFromEnd2(self, head, n):
        first = second = head
        while n >= 0:
            if second is None:
                return head.next
            else:
                second = second.next
                n -= 1
        while second:
            first = first.next
            second = second.next
        first.next = first.next.next
        return head




def ListToListNode(li):
    res = tmp = ListNode(0)
    for i in li:
        tmp.next = ListNode(i)
        tmp = tmp.next
    return res.next


def main():
    l1 = [1, 2, 3, 4, 5]
    l1 = ListToListNode(l1)
    n = 2
    s = Solution()
    res = s.removeNthFromEnd1(l1, n)
    print(ListNodeToList(res))


if __name__ == '__main__':
    main()




