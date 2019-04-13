# !/usr/bin/python3.6
# -*- coding:utf-8 -*-
# https://leetcode.com/problems/add-two-numbers/
# Approach2 is more faster


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers1(self, l1, l2):
        carry = 0
        res = tmp = ListNode(0)
        tmp1, tmp2 = l1, l2
        while tmp1 or tmp2:
            x = (tmp1.val if tmp1 is not None else 0)
            y = (tmp2.val if tmp2 is not None else 0)
            value = x + y + carry
            carry = value // 10
            tmp.next = ListNode(value % 10)
            tmp = tmp.next
            if tmp1 is not None:
                tmp1 = tmp1.next
            if tmp2 is not None:
                tmp2 = tmp2.next
        if carry > 0:
            tmp.next = ListNode(carry)
        return res.next

    def addTwoNumbers2(self, l1, l2):
        carry = 0
        res = tmp = ListNode(0)
        tmp1, tmp2 = l1, l2
        while tmp1 or tmp2:
            x = (tmp1.val if tmp1 else 0)
            y = (tmp2.val if tmp2 else 0)
            value = x + y + carry
            carry = value // 10
            tmp.next = ListNode(value % 10)
            tmp = tmp.next
            if tmp1:
                tmp1 = tmp1.next
            if tmp2:
                tmp2 = tmp2.next
        if carry > 0:
            tmp.next = ListNode(carry)
        return res.next


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
    l1 = [2, 4, 3]
    l2 = [5, 6, 4]
    l1 = ListToListNode(l1)
    l2 = ListToListNode(l2)
    s = Solution()
    res = s.addTwoNumbers2(l1, l2)
    print(ListNodeToList(res))


if __name__ == '__main__':
    main()




