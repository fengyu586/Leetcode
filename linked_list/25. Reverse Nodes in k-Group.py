# -*- coding: utf-8 -*-
# @Author  : Jing
# @FileName: 25. Reverse Nodes in k-Group.py
# @IDE: PyCharm
# Solution 1: iteration
# Solution 2: recursion




class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def construct_linked_list(n):
    header = ListNode(1)
    cur = header
    for i in range(2, n+1):
        node = ListNode(i)
        cur.next = node
        cur = cur.next
    return header


class Solution:
    def reverse(self, header):
        pre = header
        cur = header.next
        end = header
        nxt = cur.next
        while cur:
            cur.next = pre
            if not nxt:
                break
            pre = cur
            cur = nxt
            nxt = cur.next
        start = cur
        end.next = None
        return start, end


    def find_end(self, header, k):
        cur = header
        while k != 1 and cur:
            cur = cur.next
            k -= 1
        if k == 1:
            return cur
        else:
            return header

    def reverseKGroup1(self, head, k):
        if not head or k <= 1:
            return head
        cur = head
        n = 0
        while cur:
            cur = cur.next
            n += 1
        if k > n:
            return head
        if n == 1:
            return head
        groups = (n // k) - 1
        end = self.find_end(head, k)
        nxt = end.next
        end.next = None
        start = head
        start, end = self.reverse(start)
        header = start
        for _ in range(groups):
            tmp = end
            start = nxt
            end = self.find_end(start, k)
            nxt = end.next
            # split
            end.next = None
            start, end = self.reverse(start)
            # connect the two groups
            tmp.next = start
        end.next = nxt
        return header

    def reverseKGroup2(self, head, k):
        n, cur = 0, head
        while cur:
            cur = cur.next
            n += 1
        if k <= 1 or n < k:
            return head
        node, cur = None, head
        for _ in range(k):
            nxt = cur.next
            cur.next = node
            node = cur
            cur = nxt
        # connect the two groups
        head.next = self.reverseKGroup2(cur, k)
        return node


def print_linked_list(head):
    cur = head
    res = []
    while cur:
        res.append(cur.val)
        cur = cur.next
    print(res)


if __name__ == '__main__':
    n = 5
    k = 3
    head = construct_linked_list(n)
    print_linked_list(head)
    s = Solution()
    header = s.reverseKGroup2(head, k)
    print_linked_list(header)


