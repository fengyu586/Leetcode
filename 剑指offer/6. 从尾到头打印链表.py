# -*- coding: utf-8 -*-
# @Author  : Jing
# @FileName: 从尾到头打印链表.py
# @IDE: PyCharm
# https://www.nowcoder.com/practice/d0267f7f55b3412ba93bd35cfa8e8035?tpId=13&tqId=11156&tPage=1&rp=1&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking
# Solution 1: 用具有后进先出特性的栈实现从尾到头打印 O(n)Time O(1)Space
# Solution 2: 使用递归实现从尾到头打印


from base import link_node, print_linked_list


def create_linked_list():
    n = 10
    header = link_node(0)
    cur = header
    for i in range(n):
        node = link_node(i)
        cur.next = node
        cur = cur.next
    return header

class Solution:
    def print_reserved_linked_list1(self, head):
        if head is None:
            return None
        res = []
        while head:
            res.append(head.val)
            head = head.next
        while len(res) != 0:
            print(res.pop())

    def print_reserved_linked_list2(self, head):
         if head is None:
             return None
         else:
             self.print_reserved_linked_list2(head.next)
             print(head.val)



if __name__ == '__main__':
    # 创建链表
    print("Creating linked list")
    head = create_linked_list()
    cur = head

    # 打印原链表
    print("Printing origin linked list")
    print_linked_list(cur)

    # 从尾到头打印链表
    print("Printing linked list from tail to head")
    s = Solution()
    s.print_reserved_linked_list2(head)


