# -*- coding: utf-8 -*-
# @Author  : Jing
# @FileName: 38. count and say.py
# @IDE: PyCharm
# https://leetcode.com/problems/count-and-say/


class Solution:
    def countAndSay(self, n):
        cur = '1'
        if n == 1:
            return cur
        for i in range(1,n):
            j = 0
            tmp = ''
            # 对前一个人报的数进行统计
            while j < len(cur):
                count = 1
                while j+1 <len(cur) and cur[j] == cur[j+1]:
                    count += 1
                    j += 1
                tmp +=  str(count)+cur[j]
                j += 1
            cur = tmp
        return cur


if __name__ == '__main__':
    s = Solution()
    print(s.countAndSay(5))             # Output is 111221

