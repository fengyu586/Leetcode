# -*- coding: utf-8 -*-
# @Author  : Jing
# @FileName: 57.和为s的数字.py
# @IDE: PyCharm
# Solution 1: 暴力法 O(n^2)Time, O(1)Space
# Solution 2: 双指针法 O(n)Time, O(1)Space


class Solution:
    def FindNumbersWithSum1(self, array, tsum):
        # write code here
        if not array:
            return []
        product = float('inf')
        res = []
        n = len(array)
        for i in range(n-1):
            target = tsum-array[i]
            for j in range(i+1, n):
                if array[j] == target:
                    if product > array[i]*target:
                        product = array[i]*target
                        if not res:
                            res += [array[i], target]
                        else:
                            res[:] = [array[i], target]
        return res

    def FindNumbersWithSum2(self, array, tsum):
        if not array:
            return []
        n = len(array)
        res = []
        left, right = 0, n-1
        while left < right:
            cur_sum = array[left]+array[right]
            if cur_sum == tsum:
                res = [array[left], array[right]]
                break
            elif cur_sum > tsum:
                right -= 1
            else:
                left += 1
        return res


if __name__ == '__main__':
    nums = [1, 2, 4, 7, 11, 15]
    tsum = 15
    s = Solution()
    print(s.FindNumbersWithSum2(nums, tsum))


