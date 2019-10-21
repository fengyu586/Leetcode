# -*- coding: utf-8 -*-
# @Author  : Jing
# @FileName: 按之字形打印二叉树.py
# @IDE: PyCharm


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


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
    def Print(self, pRoot):
        if not pRoot:
            return []
        res = [[]]

        # flag为0表示从左到右，flag为1表示从右到左
        flag = 0
        num_leave = 0
        remain_nodes = 1
        nodes = [pRoot]
        cur_nodes = []
        while nodes or cur_nodes:
            if not nodes:
                cur_nodes, nodes = nodes, cur_nodes
            cur_node = nodes.pop()
            res[-1].append(cur_node.val)
            if flag == 0:
                if cur_node.left:
                    cur_nodes.append(cur_node.left)
                    num_leave += 1
                if cur_node.right:
                    cur_nodes.append(cur_node.right)
                    num_leave += 1
            else:
                if cur_node.right:
                    cur_nodes.append(cur_node.right)
                    num_leave += 1
                if cur_node.left:
                    cur_nodes.append(cur_node.left)
                    num_leave += 1
            remain_nodes -= 1
            if remain_nodes == 0 and num_leave != 0:
                res.append([])
                remain_nodes = num_leave
                num_leave = 0
                flag = 1-flag
        return res


if __name__ == '__main__':
    preOrder = [8, 6, 5, 7, 10, 9, 11]
    inOrder = [5, 6, 7, 8, 9, 10, 11]
    flag = reConstructBinaryTree(preOrder, inOrder)
    s = Solution()
    print(s.Print(flag))