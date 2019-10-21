# -*- coding: utf-8 -*-
# @Author  : Jing
# @FileName: 32.从上到下打印二叉树.py
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
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        if not root:
            return []
        if not isinstance(root, TreeNode):
            return []
        deque = [root]
        res = []
        while deque:
            node = deque.pop(0)
            res.append(node.val)
            if node.left:
                deque.append(node.left)
            if node.right:
                deque.append(node.right)
        return res


    def Print(self, root):
        """按层从上到下打印二叉树"""
        if not root:
            return []
        res = [[]]
        nodes = [root]
        next_level = 0
        toBePrint = 1
        while nodes:
            cur_node = nodes.pop(0)
            res[-1].append(cur_node.val)
            if cur_node.left:
                nodes.append(cur_node.left)
                next_level += 1
            if cur_node.right:
                nodes.append(cur_node.right)
                next_level += 1
            toBePrint -= 1
            if toBePrint == 0:
                if next_level != 0:
                    res.append([])
                toBePrint = next_level
                next_level = 0
        return res


if __name__ == '__main__':
    preOrder = [4, 2, 1, 3, 6, 5, 7]
    inOrder = [1, 2, 3, 4, 5, 6, 7]
    flag = reConstructBinaryTree(preOrder, inOrder)
    s = Solution()
    print(s.PrintFromTopToBottom(flag))
    print(s.Print(flag))