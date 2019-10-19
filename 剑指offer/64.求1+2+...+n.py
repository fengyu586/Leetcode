# -*- coding: utf-8 -*-
# @Author  : Jing
# @FileName: 64.py
# @IDE: PyCharm


class Solution:
    def __init__(self):
        self.sum = 0

    def Sum_Solution(self, n):
        # write code here
        def get_sum(n):
            self.sum += n
            n -= 1
            return n > 0 and self.Sum_Solution(n)

        get_sum(n)
        return self.sum


if __name__ == '__main__':
    n = 100
    s = Solution()
    print(s.Sum_Solution(n))