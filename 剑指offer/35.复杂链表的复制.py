# -*- coding: utf-8 -*-
# @Author  : Jing
# @FileName: 35.复杂链表的复制.py
# @IDE: PyCharm
# Solution 1: O(n)Time O(n)Space
# Solution 2: O(n)Time O(1)Space


class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution:
    def clone(self, pHead):
        cur = pHead
        while cur:
            node = RandomListNode(cur.label)
            node.next = cur.next
            cur.next = node
            cur = node.next
        return pHead

    def set_random(self, pHead):
        cur = pHead
        while cur :
            new_cur = cur.next
            if cur.random:
                new_cur.random = cur.random.next
            cur = new_cur.next
        return pHead

    def delete_node(self, pHead):
        cur = pHead
        new_pHead = cur.next
        while cur and cur.next and cur.next.next:
            new_cur = cur.next
            cur = new_cur.next
            new_cur.next = cur.next
        return new_pHead

    def Clone1(self, pHead):
        # write code here
        if not pHead:
            return pHead
        cur = pHead
        dic = dict()
        nodes = []
        while cur:
            nodes.append(cur)
            cur = cur.next
        cur = pHead
        while cur:
            if cur.random:
                dic[cur] = nodes.index(cur.random)
            else:
                dic[cur] = None
            cur = cur.next
        new_nodes = [RandomListNode(cur.label) for cur in nodes]
        for i, node in enumerate(nodes):
            if dic[node]:
                new_nodes[i].random = new_nodes[dic[node]]
        new_pHead = new_nodes[0]
        cur = new_pHead
        for node in new_nodes[1:]:
            cur.next = node
            cur = cur.next
        return new_pHead

    def Clone2(self, pHead):
        pHead = self.clone(pHead)
        print("After clone: ")
        print_node(pHead)
        pHead = self.set_random(pHead)
        print("After set random: ")
        print_node(pHead)
        pHead = self.delete_node(pHead)
        print("After delete: ")
        print_node(pHead)
        return pHead


def construct_linked_list(nums):
    pHead = RandomListNode(nums[0])
    cur = pHead
    for i in nums[1:]:
        node = RandomListNode(i)
        cur.next = node
        cur = cur.next
    cur = pHead
    while cur and cur.next and cur.next.next:
        nxt = cur.next.next
        cur.random = nxt
        cur = cur.next
    return pHead


def print_node(pHead):
    cur = pHead
    res = []
    while cur:
        res.append(cur.label)
        cur = cur.next
    print(res)


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6]
    pHead = construct_linked_list(nums)
    print_node(pHead)
    s = Solution()
    pHead = s.Clone1(pHead)
    print_node(pHead)
    pHead = s.Clone2(pHead)
    print_node(pHead)
