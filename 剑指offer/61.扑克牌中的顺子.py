# -*- coding: utf-8 -*-
# @Author  : Jing
# @FileName: 61.扑克牌中的顺子.py
# @IDE: PyCharm
# Solution 1: 思路：先排序，再统计数组中0的个数，
# 然后检查数组中非零数是否有重复，有则返回False，
# 无则统计数组之间的间隔，再与0的个数比较，
# 若多余0的个数，则返回False，否则返回True
# O(nlogn)Time O(1)Space
# Solution 2: 思路与解法一类似，排序通过哈希表实现 O(n)Time O(14)Space


class Solution:
    def count(self, numbers, num):
        n = len(numbers)
        res = 0
        for i in numbers:
            if i == num:
                res += 1
            if i > num:
                break
        return res

    def IsContinuous1(self, numbers):
        # write code here
        if not numbers:
            return None
        numbers = sorted(numbers)
        n = len(numbers)
        count_0 = self.count(numbers, 0)
        if count_0 > 2:
            return False
        count = 0
        for i in range(count_0 + 1, n):
            if numbers[i] == numbers[i-1]:
                return False
            count += numbers[i] - numbers[i - 1] - 1
        if count > count_0:
            return False
        else:
            return True

    def IsContinuous2(self, numbers):
        if not numbers:
            return False
        n = len(numbers)
        dic = dict(zip(list(range(14)), [0 for _ in range(14)]))
        for i in numbers:
            dic[i] += 1
        del numbers
        count_0 = dic[0]
        count = 0
        numbers = [0 for _ in range(count_0)]
        for i in range(1, 14):
            if dic[i] > 1:
                return False
            if dic[i] == 1:
                numbers.append(i)
        if len(numbers) != n:
            return False
        for i in range(count_0+1, n):
            count += numbers[i]-numbers[i-1]-1
        if count > count_0:
            return False
        else:
            return True


if __name__ == '__main__':
    numbers = [1, 3, 2, 4, 6]
    s = Solution()
    print(s.IsContinuous2(numbers))
