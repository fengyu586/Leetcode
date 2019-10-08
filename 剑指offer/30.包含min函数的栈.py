# -*- coding: utf-8 -*-
# @Author  : Jing
# @FileName: 30.包含min函数的栈.py
# @IDE: PyCharm


class Solution:
    def __init__(self):
        self.stack1, self.min_stack = [], []
    def push(self, node):
        # write code here
        self.stack1.append(node)
        if self.min_stack:
            self.min_stack.append(min(self.min_stack[-1], node))
        else:
            self.min_stack.append(node)
    def pop(self):
        # write code here
        if self.stack1:
            self.min_stack.pop()
            return self.stack1.pop()
        else:
            return None
    def top(self):
        # write code here
        if self.stack1:
            return self.stack1[-1]
        else:
            return None
    def min(self):
        # write code here
        if self.min_stack:
            return self.min_stack[-1]
        else:
            return None

