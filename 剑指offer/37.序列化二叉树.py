# -*- coding: utf-8 -*-
# @Author  : Jing
# @FileName: 37.序列化二叉树.py
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
    def __init__(self):
        self.pre_flag = -1
        self.post_flag = None

    def pre_order(self, root):
        if not root:
            s = '#,'
            return s
        s = str(root.val) + ','
        left = self.pre_order(root.left)
        right = self.pre_order(root.right)
        s += left + right
        return s

    def post_order(self, root):
        if not root:
            s = '#,'
            return s
        left = self.post_order(root.left)
        right = self.post_order(root.right)
        s = str(root.val)+','
        s = left+right+s
        return s

    def pre_order_Serialize(self, root):
        # write code here
        s = self.pre_order(root)
        return s

    def post_order_Serialize(self, root):
        s = self.post_order(root)
        return s

    def pre_deserialize(self, s):
        self.pre_flag += 1
        if self.pre_flag >= len(s):
            return None
        node = None
        if s[self.pre_flag] != '#':
            node = TreeNode(int(s[self.pre_flag]))
            node.left = self.pre_deserialize(s)
            node.right = self.pre_deserialize(s)
        return node

    def pre_order_Deserialize(self, s):
        # write code here
        s = s.split(',')
        return self.pre_deserialize(s)

    def post_order_deserialize(self, s):
        self.post_flag -= 1
        if s[self.post_flag] == '#':
            return None
        root = TreeNode(int(s[self.post_flag]))
        right = self.post_order_deserialize(s)
        if right:
            root.right = right
        left = self.post_order_deserialize(s)
        if left:
            root.left = left
        return root

    def post_order_Deserialize(self, s):
        s = s.split(',')
        self.post_flag = len(s)-1
        root = self.post_order_deserialize(s)
        return root


if __name__ == '__main__':
    preOrder = [4, 2, 1, 3, 6, 5, 7]
    inOrder = [1, 2, 3, 4, 5, 6, 7]
    flag = reConstructBinaryTree(preOrder, inOrder)
    s = Solution()
    string = s.pre_order_Serialize(flag)
    print(string)
    a = s.pre_order_Deserialize(string)
    print(s.pre_order_Serialize(a))




