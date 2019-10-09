# -*- coding: utf-8 -*-
# @Author  : Jing
# @FileName: 34.二叉树中和为某一值的路径.py
# @IDE: PyCharm


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


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def __init__(self):
        self.res = []

    def get_path(self, root, cur_val, expectNumber, path, depth):
        path.append(root)
        cur_val += root.val
        if not root.left and not root.right:
            if  cur_val == expectNumber:
                self.res.append(([node.val for node in path], depth))
            path.pop()
            cur_val -= root.val
            return
        if root.left:
            self.get_path(
                root.left,
                cur_val,
                expectNumber,
                path,
                depth + 1)
        if root.right:
            self.get_path(
                root.right,
                cur_val,
                expectNumber,
                path,
                depth + 1)
        path.pop()
        cur_val -= root.val

    def FindPath(self, root, expectNumber):
        # write code here
        if not root:
            return []
        cur_val, path, depth = 0, [], 0
        self.get_path(root, cur_val, expectNumber, path, depth)
        res = sorted(self.res, key=lambda x: x[1], reverse=True)
        result = [tmp[0] for tmp in res]
        return result


if __name__ == '__main__':
    preOrder = [10, 5, 4, 7, 12]
    inOrder = [4, 5, 7, 10, 12]
    target = 22
    flag = reConstructBinaryTree(preOrder, inOrder)
    s = Solution()
    print(s.FindPath(flag, target))