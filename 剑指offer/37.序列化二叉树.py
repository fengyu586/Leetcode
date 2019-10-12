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
        self.flag = -1

    def pre_order(self, root, s):
        if not root:
            s = '#,'
            return s
        s = str(root.val) + ','
        left = self.pre_order(root.left, s)
        right = self.pre_order(root.right, s)
        s += left + right
        return s

    def Serialize(self, root):
        # write code here
        s = ''
        s = self.pre_order(root, s)
        return s

    def Deserialize(self, s):
        # write code here
        self.flag += 1
        l = s.split(',')
        if self.flag >= len(s):
            return None
        node = None
        if l[self.flag] != '#':
            node = TreeNode(int(l[self.flag]))
            node.left = self.Deserialize(s)
            node.right = self.Deserialize(s)
        return node


if __name__ == '__main__':
    preOrder = [4, 2, 1, 3, 6, 5, 7]
    inOrder = [1, 2, 3, 4, 5, 6, 7]
    flag = reConstructBinaryTree(preOrder, inOrder)
    s = Solution()
    string = s.Serialize(flag)
    print(string)
    a = s.Deserialize(string)
    print(s.Serialize(a))




