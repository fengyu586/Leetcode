# -*- coding: utf-8 -*-
# @Author  : Jing
# @FileName: 108. Convert Sorted Array to Binary Search Tree.py
# @IDE: PyCharm
# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
from base import TreeNode, PrintTree


class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        mid = (len(nums)-1) >> 1
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        return root


if __name__ == '__main__':
    nums = [-10, -3, 0, 5, 9]
    s = Solution()
    root = s.sortedArrayToBST(nums)
    p = PrintTree()
    p.in_order(root)
    p.print_tree()
