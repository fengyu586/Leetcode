# -*- coding: utf-8 -*-
# @Author  : Jing
# @FileName: 82. Remove Duplicates from Sorted List II.py
# @IDE: PyCharm
# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
from base import contruct_linked_list, print_linked_list


class Solution:
    def deleteDuplicates1(self, head):
        if not head:
            return None
        pre = header = None
        cur = head
        while cur and cur.next:
            nxt = cur.next
            if cur.val == nxt.val:
                while nxt and nxt.val == cur.val:
                    nxt = nxt.next
            elif pre:
                pre.next = cur
                pre = pre.next
            else:
                header = pre = cur
            cur = nxt
        if pre:
            pre.next = cur
        else:
            header = cur
        return header

    def deleteDuplicates2(self, head):
        if not head:
            return head
        if head.next and head.val == head.next.val:
            while head.next and head.next.val == head.val:
                head = head.next
            return self.deleteDuplicates2(head.next)
        else:
            head.next = self.deleteDuplicates2(head.next)
            return head


if __name__ == '__main__':
    nums = [1, 2, 3, 3, 4, 4, 5]
    head = contruct_linked_list(nums)
    s = Solution()
    head = s.deleteDuplicates2(head)
    print_linked_list(head)




