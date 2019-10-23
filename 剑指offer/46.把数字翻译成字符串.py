# -*- coding: utf-8 -*-
# @Author  : Jing
# @FileName: 46.把数字翻译成字符串.py
# @IDE: PyCharm
# Solution: f(n)表示前n+1数字的表示方法有多少种，
# f(n,0)表示s[n]和s[n-1]未合并的情况下，有多少种表示方法。
# f(n,1)表示s[n]和s[n-1]合并的情况下，有多少种表示方法。
# 状态转移方程：
# 不合并的情况：f(n,0) = f(n-1,0)+f(n-1,1)，
# 合并的情况：
# 若s[n]和s[n-1]可合并，则flag = 1，否则为0
# f(n,1) = f(n-1,0)*flag
# 初始条件: f(0,0)=1,f(0,1)=0
# 顺序：0，1，...，n


class Solution:
    def getTranslationCount(self, string):
        if not string:
            return 0
        n = len(string)
        dp = [[0, 0] for _ in range(n)]
        dp[0][0], dp[0][1] = 1, 0
        for i in range(1, n):
            if 10 <= int(string[i-1]+string[i]) < 26:
                flag = 1
            else:
                flag = 0
            dp[i][0] = dp[i-1][1]+dp[i-1][0]
            dp[i][1] = dp[i-1][0]*flag
        return sum(dp[n-1])


if __name__ == '__main__':
    string = '12258'
    s = Solution()
    print(s.getTranslationCount(string))



