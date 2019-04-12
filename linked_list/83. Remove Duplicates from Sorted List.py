#!/usr/bin/python3.6
# -*- coding:utf-8 -*-
# https://leetcode.com/problems/remove-duplicates-from-sorted-list/


class Solution:
    def deleteDuplicates(self, head):
        old_list = new_list = head
        if not(head):
            return head
        while head.next:
            head = head.next
            if new_list.val != head.val:
                new_list.next = head
                new_list = new_list.next
        if new_list.next:
            new_list.next = None
        return old_list

