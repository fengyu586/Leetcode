# -*- coding: utf-8 -*-
# @Author  : Jing
# @FileName: 二叉搜索树的第k个结点.py
# @IDE: PyCharm


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def reConstructBinaryTree(pre, tin):
    """根据先序遍历序列和中序遍历序列构建二叉树"""
    if len(pre) == 0 or len(tin) == 0:
        return None
    if len(pre) == 1:
        return TreeNode(pre[0])
    else:
        flag = TreeNode(pre[0])
        index = tin.index(pre[0])
        flag.left = reConstructBinaryTree(pre[1:index + 1],
                                          tin[:index])
        flag.right = reConstructBinaryTree(pre[index + 1:],
                                           tin[index + 1:])
    return flag


class Solution:
    # 返回对应节点TreeNode
    def get_number(self, pRoot, count, res):
        if not pRoot:
            return 0
        count += 1
        res.append(pRoot)
        if pRoot.left:
            count = self.get_number(pRoot.left, count, res)
        if pRoot.right:
            count = self.get_number(pRoot.right, count, res)
        return count

    def location(self, nums, start, end):
        left, right = start, end
        node = nums[left]
        while left < right:
            while left < right and nums[right].val >= node.val:
                right -= 1
            nums[left] = nums[right]
            while left < right and nums[left].val < node.val:
                left += 1
            nums[right] = nums[left]
        nums[left] = node
        return left

    def KthNode(self, pRoot, k):
        # write code here
        if not pRoot or k <= 0:
            return None
        count, res = 0, []
        count = self.get_number(pRoot, count, res)
        if count < k:
            return None
        start, end = 0, count - 1
        index = self.location(res, start, end)
        while 0 <= index < count and index != k-1:
            if index > k-1:
                end = index - 1
            else:
                start = index + 1
            index = self.location(res, start, end)
        return res[index].val


if __name__ == '__main__':
    preOrder = [8, 6, 5, 7, 10, 9, 11]
    inOrder = [5, 6, 7, 8, 9, 10, 11]
    flag = reConstructBinaryTree(preOrder, inOrder)
    k = 4
    s = Solution()
    print(s.KthNode(flag, k))
