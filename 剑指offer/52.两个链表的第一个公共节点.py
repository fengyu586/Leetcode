# -*- coding: utf-8 -*-
# @Author  : Jing
# @FileName: 52.两个链表的第一个公共节点.py
# @IDE: PyCharm




class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def construct_linked_list(nums):
    pHead = ListNode(nums[0])
    cur = pHead
    for i in nums[1:]:
        node = ListNode(i)
        cur.next = node
        cur = cur.next
    cur = pHead
    while cur and cur.next and cur.next.next:
        nxt = cur.next.next
        cur.random = nxt
        cur = cur.next
    return pHead


class Solution:
    def get_nodes1(self, pHead):
        nodes = []
        if not pHead:
            return nodes
        while pHead:
            nodes.append(pHead)
            pHead = pHead.next
        return nodes

    def FindFirstCommonNode1(self, pHead1, pHead2):
        # write code here
        if not pHead1 or not pHead2:
            return None
        nodes1 = self.get_nodes1(pHead1)
        nodes2 = self.get_nodes1(pHead2)
        node = None
        while nodes1 and nodes2 and nodes1[-1].val == nodes2[-1].val:
            node = nodes1.pop()
            nodes2.pop()
        return node

    def get_nodes2(self, pHead):
        nodes = []
        count = 0
        if not pHead:
            return nodes, count
        while pHead:
            count += 1
            nodes.append(pHead.val)
            pHead = pHead.next
        return nodes, count

    def FindFirstCommonNode2(self, pHead1, pHead2):
        # write code here
        if not pHead1 or not pHead2:
            return None
        cur1, cur2 = pHead1, pHead2
        nodes1, n1 = self.get_nodes2(cur1)
        nodes2, n2 = self.get_nodes2(cur2)
        while nodes1 and nodes2 and nodes1[-1] == nodes2[-1]:
            n1 -= 1
            n2 -= 1
            nodes1.pop()
            nodes2.pop()
        pHead = pHead1 if n1 < n2 else pHead2
        n = n1 if n1 < n2 else n2
        while n > 0:
            pHead = pHead.next
            n -= 1
        return pHead


def print_node(pHead):
    cur = pHead
    res = []
    while cur:
        res.append(cur.val)
        cur = cur.next
    print(res)


if __name__ == '__main__':
    nums1 = [1, 2, 3, 4, 5, 6]
    pHead1 = construct_linked_list(nums1)
    print_node(pHead1)
    nums2 = [3, 2, 1, 4, 5, 6]
    pHead2 = construct_linked_list(nums2)
    print_node(pHead2)
    s = Solution()
    print_node(s.FindFirstCommonNode2(pHead1, pHead2))

