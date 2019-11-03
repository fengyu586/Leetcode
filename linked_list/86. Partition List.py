# -*- coding: utf-8 -*-
# @Author  : Jing
# @FileName: 86. Partition List.py
# @IDE: PyCharm
# https://leetcode.com/problems/partition-list/
# two pointer method:O(n)Time O(1)Space
from base import contruct_linked_list, print_linked_list, ListNode


class Solution:
    def partition(self, head, x: int):
        if not head:
            return None
        before_head = ListNode(0)
        after_head = ListNode(0)
        before_cur = before_head
        after_cur = after_head
        while head:
            if head.val < x:
                before_cur.next = head
                before_cur = before_cur.next
            else:
                after_cur.next = head
                after_cur = after_cur.next
            head = head.next
        after_cur.next = None
        before_cur.next = after_head.next
        return before_head.next


if __name__ == '__main__':
    nums = [1, 4, 3, 2, 5, 2]
    x = 3
    head = contruct_linked_list(nums)
    s = Solution()
    head = s.partition(head, x)
    print_linked_list(head)
