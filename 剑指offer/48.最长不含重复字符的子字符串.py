# -*- coding: utf-8 -*-
# @Author  : Jing
# @FileName: 48.最长不含重复字符的子字符串.py
# @IDE: PyCharm


class Solution:
    def longestSubstringWithoutDuplication(self, string):
        if not string:
            return 0
        n = len(string)
        dic = {string[0]:0}
        dp = [0 for _ in range(n)]
        dp[0] = 1
        for i in range(1, n):
            if string[i] not in dic:
                dp[i] = dp[i-1]+1
                dic[string[i]] = i
            else:
                if i-dic[string[i]] > dp[i-1]:
                    dp[i] = dp[i-1]+1
                else:
                    dp[i] = i-dic[string[i]]
        return dp[-1]


if __name__ == '__main__':
    string = 'arabcacfr'
    s = Solution()
    print(s.longestSubstringWithoutDuplication(string))

