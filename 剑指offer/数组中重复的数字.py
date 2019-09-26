# -*- coding: utf-8 -*-
# @Author  : Jing
# @FileName: 数组中重复的数字.py
# @IDE: PyCharm
# https://www.nowcoder.com/practice/529d3ae5a407492994ad2a246518148a?tpId=13&tqId=11167&tPage=1&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking


class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        dic = dict()
        res = None
        for i in numbers:
            if i in dic:
                dic[i] += 1
                res = i
                break
            else:
                dic[i] = 1
        if res is not None:
            duplication[0] = res
            return True, res
        else:
            return False, res

s = Solution()
nums = [2, 1, 3, 1, 4]
d = [0]
print(s.duplicate(nums, d))         # Output is (True, 1).
