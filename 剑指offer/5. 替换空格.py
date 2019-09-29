# -*- coding: utf-8 -*-
# @Author  : Jing
# @FileName: 5. 替换空格.py
# @IDE: PyCharm
# Solution 1: 暴力解 O(n^2)Time
# Solution 2: O(n)Time


class Solution:
    @classmethod
    def replace_null1(self, string):
        if string is None:
            return None
        n = len(string)
        count = 0
        for i in string:
            if i == ' ':
                count += 1
        res = ['' for _ in range(n+count*2)]
        res[:n] = string
        # 遍历原字符串， 若为空字符则其后续字符向后移动
        i = 0
        step = 2
        while i < n:
            if res[i] == ' ':
                for j in range(n-1, i, -1):
                    res[j+step] = res[j]
                n += step
                res[i:i+3] = "%20"
                i += 3
            else:
                i += 1
        return ''.join(res)

    @classmethod
    def replace_null2(self, string):
        if not string:
            return None
        count = 0
        for i in string:
            if i == ' ':
                count += 1
        n = len(string)
        res = [' ' for _ in range(n+2*count)]
        res[:n] = string
        fast, slow = n-1, n+2*count-1
        while fast != 0:
            if res[fast] != " ":
                res[slow] = res[fast]
                fast -= 1
                slow -= 1
            else:
                res[slow-2: slow+1] = "%20"
                slow -= 3
                fast -= 1
        return ''.join(res)


if __name__ == '__main__':
    strings = "We are happy."
    s = Solution()
    print(s.replace_null2(strings))     # Output is We%20are%20happy.



