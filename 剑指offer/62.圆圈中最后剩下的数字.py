# -*- coding: utf-8 -*-
# @Author  : Jing
# @FileName: 62.圆圈中最后剩下的数字.py
# @IDE: PyCharm
# Solution 1: O(mn)Time O(n)Space
# Solution 2: O(n)Time O(1)Space


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def construct_linked_list(self, n):
        header = Node(0)
        cur = header
        for i in range(1, n):
            node = Node(i)
            cur.next = node
            cur = cur.next
        cur.next = header
        return header

    def LastRemaining_Solution(self, n, m):
        # write code here
        if n < 1 or m < 1:
            return -1
        if m == 1:
            return n-1
        header = self.construct_linked_list(n)
        cur = header
        index = 0
        while cur.next.val != cur.val:
            if index == m-2:
                cur.next = cur.next.next
                index = 0
            else:
                index += 1
            cur = cur.next
        return cur.val

    def LastRemaining_Solution2(self, n, m):
        if n < 1 or m < 1:
            return -1
        last = 0
        for i in range(2, n+1):
            last = (last+m)%i
        return last


if __name__ == '__main__':
    n, m = 5, 3
    s = Solution()
    print(s.LastRemaining_Solution2(n, m))



