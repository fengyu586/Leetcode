# -*- coding: utf-8 -*-
# @Author  : Jing
# @FileName: 7.  重建二叉树.py
# @IDE: PyCharm
# https://www.nowcoder.com/practice/
# 8a19cbe657394eeaac2f6ea9b0f6fcf6?
# tpId=13&tqId=11157&tPage=1&rp=1&ru=/ta/
# coding-interviews&qru=/ta/coding-interviews/question-ranking
from base import TreeNode


class Solution:
    def reConstructBinaryTree1(self, pre, tin):
        """根据先序遍历序列和中序遍历序列构建二叉树"""
        if len(pre) == 0 or len(tin) == 0:
            return None
        if len(pre) == 1:
            return TreeNode(pre[0])
        else:
            flag = TreeNode(pre[0])
            index = tin.index(pre[0])
            flag.left = self.reConstructBinaryTree1(pre[1:index+1],
                                                   tin[:index])
            flag.right = self.reConstructBinaryTree1(pre[index+1:],
                                                    tin[index+1:])
        return flag

    def reConstructBinaryTree2(self, tin, post):
        """根据中序遍历序列和后序遍历序列构建二叉树"""
        if len(tin) == 0 or len(post) == 0:
            return None
        if len(tin) == 1:
            return TreeNode(tin[0])
        else:
            flag = TreeNode(post[-1])
            index = tin.index(post[-1])
            flag.left = self.reConstructBinaryTree2(tin[:index], post[:index])
            flag.right = self.reConstructBinaryTree2(tin[index+1:], post[index:-1])
        return flag

    def pre_order(self, root):
        """先序遍历"""
        res = []
        def traversal(root):
            if not root:
                return None
            else:
                res.append(root.val)
                traversal(root.left)
                traversal(root.right)
        traversal(root)
        return res

    def in_order(self, root):
        """中序遍历"""
        res = []
        def traversal(root):
            if not root:
                return None
            else:
                traversal(root.left)
                res.append(root.val)
                traversal(root.right)
        traversal(root)
        return res

    def post_order(self, root):
        """后序遍历"""
        res = []
        def traversal(root):
            if not root:
                return None
            else:
                traversal(root.left)
                traversal(root.right)
                res.append(root.val)
        traversal(root)
        return res




if __name__ == '__main__':
    preOrder = [1, 2, 4, 7, 3, 5, 6, 8]
    inOrder = [4, 7, 2, 1, 5, 3, 8, 6]
    postOrder = [7, 4, 2, 5, 8, 6, 3, 1]
    s = Solution()
    flag = s.reConstructBinaryTree2(inOrder, postOrder)
    print("pre_order: ", s.pre_order(flag))
    print("in_order: ", s.in_order(flag))
    print("post_order: ", s.post_order(flag))

