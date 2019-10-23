# -*- coding: utf-8 -*-
# @Author  : Jing
# @FileName: 44.数字序列中某一位的数字.py
# @IDE: PyCharm


class Solution:
    def countOfInteger(self, digits):
        if digits == 1:
            return 10
        else:
            return 9*10**(digits-1)

    def beginDigit(self, digits):
        if digits == 1:
         return 0
        else:
            return 10**(digits-1)

    def digitAtIndex(self, index):
        if index < 0:
            return -1
        i = 1
        while True:
            number = self.countOfInteger(i)*i
            if number <= index:
                index -= number
            else:
                break
            i += 1
        number = self.beginDigit(i)
        index1, index2 = index // i, index % i
        number += index1
        i -= index2
        while i > 1:
            number //= 10
            i -= 1
        return number % 10


if __name__ == '__main__':
    n = 19
    s = Solution()
    print(s.digitAtIndex(n))

