#!/usr/bin/python3.6
# -*- coding:utf-8 -*-
# https://leetcode.com/problems/merge-k-sorted-lists/
# Approach 1:Brute Force
# Traverse all the linked lists and collect the values of the nodes into an array.
# Sort and iterate over this array to get the proper value of nodes.
# Create a new sorted linked list and extend it with the new nodes.
# Approach 2, 3, 5:  recursion, Compare one by one
# Approach 4: iteration, Compare one by one
# Approach 6: by from operator import attrgetter
# Approach 7:







class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists1(self, lists):
        self.node = []
        for li in lists:
            while li:
                self.node += [li.val]
                li = li.next
        self.node.sort()
        head = cur = ListNode(0)
        for i in self.node:
            cur.next = ListNode(i)
            cur = cur.next
        return head.next

    def mergeKLists2(self, lists):
        def find_min(lists, head):
            while None in lists:
                lists.remove(None)
            if len(lists) == 0:
                return
            min_node = lists[0]
            min_val = min_node.val
            for node in lists:
                print(node.val)
                if min_val > node.val:
                    min_val = node.val
                    min_node = node
            idx = lists.index(min_node)
            lists[idx] = lists[idx].next
            head.next = min_node
            print(min_node.val)
            find_min(lists, head.next)
            return min_node

        head = ListNode(0)
        find_min(lists, head)
        return head.next

    def mergeKLists3(self, lists):
        def find_min(lists, head):
            while None in lists:
                lists.remove(None)
            if len(lists) == 0:
                return
            min_node = lists[0]
            min_val = min_node.val
            min_index = 0
            for i in range(len(lists)):
                cur_val = lists[i].val
                if min_val > cur_val:
                    min_val = cur_val
                    min_node = lists[i]
                    min_index = i
            lists[min_index] = lists[min_index].next
            head.next = min_node
            find_min(lists, head.next)
            return min_node

        head = ListNode(0)
        find_min(lists, head)
        return head.next

    def mergeKLists4(self, lists):
        head = cur = ListNode(0)
        while lists:
            while None in lists:
                lists.remove(None)
            if len(lists) == 0:
                return head.next
            min_node = lists[0]
            min_index = 0
            for i in range(len(lists)):
                if min_node.val > lists[i].val:
                    min_node = lists[i]
                    min_index = i
            cur.next = min_node
            lists[min_index] = lists[min_index].next
            cur = cur.next
        return head.next

    def mergeKLists5(self, lists):
        def find_min(lists):
            while None in lists:
                lists.remove(None)
            if len(lists)==0:
                return None
            min_node = lists[0]
            min_index = 0
            for i in range(len(lists)):
                if min_node.val > lists[i].val:
                    min_node = lists[i]
                    min_index = i
            lists[min_index] = lists[min_index].next
            min_node.next = find_min(lists)
            return min_node
        return find_min(lists)

    def mergeKLists6(self, lists):
        from operator import attrgetter
        sorted_list = []
        for head in lists:
            curr = head
            while curr is not None:
                sorted_list.append(curr)
                curr = curr.next

        sorted_list = sorted(sorted_list, key=attrgetter('val'))
        for i, node in enumerate(sorted_list):
            try:
                node.next = sorted_list[i + 1]
            except Exception:
                node.next = None

        if sorted_list:
            return sorted_list[0]
        else:
            return None

    # def mergeKLists7(self, lists):



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
    l1 = [[1, 4, 5], [1, 3, 4], [2, 6]]
    l1 = [ListToListNode(i) for i in l1]
    l2 = [[], []]
    l2 = [ListToListNode(i) for i in l2]
    s = Solution()
    res = s.mergeKLists6(l1)
    res = ListNodeToList(res)
    print(res)


if __name__ == '__main__':
    main()













