# -*- coding: utf-8 -*-
# @Author  : Jing
# @FileName: 9.用两个栈实现队列.py
# @IDE: PyCharm


class Deque:
    """用两个栈实现队列"""
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, val):
        self.stack1.append(val)

    def pop(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()


class Stack:
    def __init__(self):
        self.deque1 = []
        self.deque2 = []

    def push(self, val):
        self.deque1.append(val)

    def pop(self):
        val = None
        if len(self.deque1)>1:
            while len(self.deque1) != 1:
                self.deque2.append(self.deque1.pop(0))
            val = self.deque1.pop(0)
            while self.deque2:
                self.deque1.append(self.deque2.pop(0))
        elif len(self.deque1) == 1:
            val = self.deque1.pop(0)
        return val



if __name__ == '__main__':
    deque = Deque()
    for i in range(5):
        deque.push(i)
    for i in range(2):
        print(deque.pop())
    deque.push(1)
    print(deque.pop())
    deque.push(4)
    while deque.stack2 or deque.stack1:
        print(deque.pop())
    # stack = Stack()
    # for i in range(5):
    #     stack.push(i)
    # while stack.deque1:
    #     print(stack.pop())





