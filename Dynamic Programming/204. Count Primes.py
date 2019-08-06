#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""====================================
# @Time    : 2019/8/7 1:17
# @Author  : Jing
# @FileName: 204. Count Primes.py
# @IDE: PyCharm
======================================="""
# https://leetcode.com/problems/count-primes/



class Solution:
    def countPrimes(self, n):
        if n <= 2:
            return 0
        res = [True]*n
        res[0] = res[1] = False
        for i in range(2, n):
            if res[i] is True:
                for j in range(2, (n-1)//i+1):
                    res[i*j] = False
        return sum(res)


