# -*- coding: utf-8 -*-
# @Author  : Jing
# @FileName: 49.丑数.py
# @IDE: PyCharm
# Solution 1: 暴力法
# Solution 2: 以空间换时间

class Solution:
    def IsUgly(self, number):
        while number % 2 == 0:
            number //= 2
        while number % 3 == 0:
            number //= 3
        while number % 5 == 0:
            number //= 5
        if number == 1:
            return True
        else:
            return False


    def GetUglyNumber_Solution1(self, index):
        # write code here
        if index <= 0:
            return 0
        count = 0
        number = 1
        while count < index:
            if self.IsUgly(number):
                count += 1
            number += 1
        return number - 1

    def Min(self, num1, num2, num3):
        return min(min(num1, num2), num3)

    def GetUglyNumber_Solution2(self, index):
        # write code here
        if index <= 0:
            return 0
        ugly_nums = [0 for i in range(index)]
        ugly_nums[0] = 1
        next_index = 1
        idx2, idx3, idx5 = 0, 0, 0
        while next_index < index:
            min_val = self.Min(ugly_nums[idx2] * 2, ugly_nums[idx3] * 3, ugly_nums[idx5] * 5)
            ugly_nums[next_index] = min_val
            while ugly_nums[idx2] * 2 <= min_val:
                idx2 += 1
            while ugly_nums[idx3] * 3 <= min_val:
                idx3 += 1
            while ugly_nums[idx5] * 5 <= min_val:
                idx5 += 1
            next_index += 1
        return ugly_nums[index - 1]

if __name__ == '__main__':
    num = 14
    s = Solution()
    print(s.GetUglyNumber_Solution2(num))