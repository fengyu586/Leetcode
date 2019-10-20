# -*- coding: utf-8 -*-
# @Author  : Jing
# @FileName: 59.滑动窗口的最大值.py
# @IDE: PyCharm
# Solution 1: 暴力法 O(kn)Time O(n)Space
# Solution 2: O(n)Time O(n)Space


class Solution:
    def maxInWindows1(self, num, size):
        if not num or size == 0 or size > len(num):
            return []
        n = len(num)
        if size == n:
            return [max(num)]
        res = []
        for i in range(n-size+1):
            res.append(max(num[i:i+size]))
        return res

    def maxInWindows2(self, num, size):
        # write code here
        if not num or size == 0:
            return []
        n = len(num)
        if size == n:
            return [max(num)]
        if size > n:
            return []
        res = []
        deque = []
        for i in range(n):
            if len(deque)>0 and i-deque[0] >= size:
                deque.pop(0)
            while len(deque) > 0 and num[i] > num[deque[-1]]:
                deque.pop()
            deque.append(i)
            if i >= size-1:
                res.append(num[deque[0]])
        return res


if __name__ == '__main__':
    nums = [2,3,4,2,6,2,5,1]
    k = 3
    s = Solution()
    print(s.maxInWindows1(nums, k))



