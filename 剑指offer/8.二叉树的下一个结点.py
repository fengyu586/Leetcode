# -*- coding: utf-8 -*-
# @Author  : Jing
# @FileName: 8.二叉树的下一个结点.py
# @IDE: PyCharm
# 题目：给定一棵二叉树和其中一个结点，
# 如何找出中序遍历的下一个结点？
# 树中的结点除了有两个分别指向左、右子结点的指针，
# 还有一个指向父结点的指针。


class Solution:
    def binary_tree_node_get_next(self, tree_node):
        if not tree_node:
            return None
        next_node = None

        # 若该结点有右子树，则下一个结点为右子树的最左结点
        if tree_node.right:
            next_node = tree_node.right
            while next_node.left:
                next_node = next_node.left

        # 若该结点无右子树，则分两种情况讨论。
        # 其一，该结点为父结点的右子节点，则不断向父结点方向遍历，
        # 直至找到某一结点为父结点的左子节点。其父结点即为下一个结点
        elif tree_node.next:
            cur_node = tree_node
            parent_node = tree_node.next
            while parent_node and parent_node.right == cur_node:
                cur_node = parent_node
                parent_node = cur_node.next
            next_node = parent_node

        # 其二，该结点为父结点的左子节点，则下一个结点为其父结点。
        return next_node





