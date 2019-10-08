# -*- coding: utf-8 -*-
# @Author  : Jing
# @FileName: 31.栈的压入、弹出序列.py
# @IDE: PyCharm


def IsPopOrder(pushV, popV):
    # write code here
    if not pushV or not popV:
        return False
    if len(pushV) != len(popV):
        return False
    stack = []
    push_idx, pop_idx = 0, 0
    while pop_idx < len(popV):
        if popV[pop_idx] in pushV[push_idx:]:
            while popV[pop_idx] != pushV[push_idx]:
                stack.append(pushV[push_idx])
                push_idx += 1
            stack.append(pushV[push_idx])
            push_idx += 1
        elif stack and stack[-1] == popV[pop_idx]:
            stack.pop()
            pop_idx += 1
        else:
            return False
    return True


if __name__ == '__main__':
    nums1 = [1, 2, 3, 4, 5]
    nums2 = [4, 3, 5, 1, 2]
    print(IsPopOrder(nums1, nums2))