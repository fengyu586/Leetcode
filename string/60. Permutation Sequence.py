# -*- coding: utf-8 -*-
# @Author  : Jing
# @FileName: 60. Permutation Sequence.py
# @IDE: PyCharm
# Solution 1: recursion
# Solution 2: iteration


class Solution:
    def __init__(self):
        self.res = []

    def generate(self, string, k, count):
        if len(string) == 1:
            self.res += string
            return
        index = k // count
        k %= count
        count //= len(string)-1
        self.res.append(string[index])
        new_string = string[:index]+string[index+1:]
        return self.generate(new_string,  k, count)

    def getPermutation1(self, n, k):
        if n <= 0:
            return ''
        count = 1
        for i in range(2, n):
            count *= i
        if n*count < k:
            return ''
        string = list(map(str, range(1, n + 1)))
        self.generate(string, k-1, count)
        return ''.join(self.res)

    def getPermutation2(self, n, k):
        if n <= 0:
            return ''
        count = 1
        for i in range(2, n):
            count *= i
        if k > n*count:
            return ''
        string = list(map(str, range(1, n+1)))
        res = []
        k -= 1
        while len(string) != 1:
            index = k//count
            res.append(string[index])
            k %= count
            count //= len(string) - 1
            string = string[:index]+string[index+1:]
        res += string
        return ''.join(res)


if __name__ == '__main__':
    n, k = 3, 3
    s = Solution()
    print(s.getPermutation2(n, k))
