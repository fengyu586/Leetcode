# -*- coding: utf-8 -*-
# @Author  : Jing
# @FileName: 18.删除链表中的重复节点.py
# @IDE: PyCharm


def deleteDuplication(pHead):
    # write code here
    # 考虑特殊情况
    if pHead is None:
        return None
    pre = None
    cur = pHead
    while cur:
        nxt = cur.next
        need_delete = False         # 标志是否有重复节点
        if nxt and nxt.val == cur.val:
            need_delete = True
        if not need_delete:
            pre = cur
            cur = cur.next
        else:
            val = cur.val
            while cur and cur.val == val:
                nxt = cur.next
                cur = nxt
            if not pre:         # 检查pre是否是空指针
                pHead = cur
            else:
                pre.next = cur
    return pHead