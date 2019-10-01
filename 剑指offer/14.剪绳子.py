# -*- coding: utf-8 -*-
# @Author  : Jing
# @FileName: 14.剪绳子.py
# @IDE: PyCharm
# Solution 1: DP O(n^2)Time O(n)Space
# Solution 2: greed algorithm O(1)Time, O(1)Space


def cut_rop1(n):
    # 边界条件
    if n < 2:
        return 0
    if n <= 3:
        return n-1
    dp = [0 for _ in range(n+1)]

    # 初始化条件，当绳子的长度小于4时，将其当作独立的一部分不再裁剪
    for i in range(4):
        dp[i] = i

    # dp[i]表示绳子长为i时剪成若干段后，各段长度乘积的最大值
    # 状态转移方程：dp[i] = max(dp[i], dp[j]*dp[j-i]), 1<=j<=(i//2)+1
    for i in range(4, n+1):
        for j in range(1, (i//2)+1):
            dp[i] = max(dp[i], dp[j]*dp[i-j])
    return dp[n]

def cut_rop2(n):
    # 尽可能多剪出长度为3或2的绳子
    if n < 2:
        return 0
    if n <= 3:
        return n-1
    times_of_3 = n // 3
    if n - times_of_3 * 3 == 1:
        times_of_3 -= 1
    times_of_2 = (n-times_of_3*3)//2
    return 3**times_of_3*2**times_of_2


if __name__ == '__main__':
    n = 0
    print(cut_rop2(n))
