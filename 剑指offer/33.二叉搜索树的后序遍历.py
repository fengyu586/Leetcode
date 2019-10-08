# -*- coding: utf-8 -*-
# @Author  : Jing
# @FileName: 33.二叉搜索树的后序遍历.py
# @IDE: PyCharm


def VerifySquenceOfBST(sequence):
    # write code here
    if not sequence:
        return None
    root = sequence[-1]
    i = 0
    while i < len(sequence) - 1:
        if sequence[i] < root:
            i += 1
        else:
            break
    j = i
    # 若在右子树中有一个节点的值小于根节点，则返回False
    while j < len(sequence) - 1:
        if sequence[j] > root:
            j += 1
        else:
            return False
    left = True if sequence[0] <= root else False
    if i > 0:
        left = VerifySquenceOfBST(sequence[:i])
    right = True if sequence[i] >= root else False
    if j < len(sequence) - 1:
        right = VerifySquenceOfBST(sequence[j:-1])
    return left and right


if __name__ == '__main__':
    nums = [4, 8, 6, 12, 16, 14, 10]
    print(VerifySquenceOfBST(nums))
