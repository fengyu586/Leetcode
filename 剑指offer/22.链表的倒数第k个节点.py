# -*- coding: utf-8 -*-
# @Author  : Jing
# @FileName: 22.链表的倒数第k个节点.py
# @IDE: PyCharm


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def construct_linked_list(nums):
    header = Node(nums[0])
    cur = header
    for i in nums[1:]:
        node = Node(i)
        cur.next = node
        cur = cur.next
    return header


class Solution:
    def FindLastK(self, header, k):
        if not header or k <= 0:
            return None
        cur = header
        n = 0
        while cur:
            n += 1
            cur = cur.next
        if n < k:
            return None
        cur = header
        nxt = header
        while k != 0:
            nxt = nxt.next
            k -= 1
        while nxt:
            cur = cur.next
            nxt = nxt.next
        return cur.val


if __name__ == '__main__':
    nums = list(range(5))
    print(nums)
    k = 2
    header = construct_linked_list(nums)
    s = Solution()
    print(s.FindLastK(header, k))



