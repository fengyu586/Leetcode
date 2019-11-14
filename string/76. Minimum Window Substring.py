# -*- coding: utf-8 -*-
# @Author  : Jing
# @FileName: 76. Minimum Window Substring.py
# @IDE: PyCharm
# https://leetcode.com/problems/minimum-window-substring/
# Solution 1: SlidingWindows
# Solution 2: Optimized


class Solution:
    def minWindow1(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        required = len(set(t))
        dic = {}
        for sub_t in t:
            dic[sub_t] = dic.get(sub_t, 0) + 1
        l, r = 0, 0
        windows_dic = {}
        formed = 0
        res = float('inf'), None, None
        while r < len(s):
            char = s[r]
            windows_dic[char] = windows_dic.get(char, 0) + 1
            if char in dic and windows_dic[char] == dic[char]:
                formed += 1
            while l <= r and formed == required:
                char = s[l]
                if r-l+1 < res[0]:
                    res = r-l+1, l, r
                windows_dic[char] -= 1
                if char in dic and windows_dic[char] < dic[char]:
                    formed -= 1
                l += 1
            r += 1
        return ''if res[0] == float('inf')else s[res[1]:res[2]+1]

    def minWindow2(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        required = len(set(t))
        formed, l, r = 0, 0, 0
        dic, windows_dic, filter_s = {}, {}, []
        res = float("inf"), None, None
        for sub in t:
            dic[sub] = dic.get(sub, 0) + 1
        for i, sub in enumerate(s):
            if sub in dic:
                filter_s.append([i, sub])
        while r < len(filter_s):
            char = filter_s[r][1]
            windows_dic[char] = windows_dic.get(char, 0) + 1
            if char in dic and windows_dic[char] == dic[char]:
                formed += 1
            while l <= r and formed == required:
                char = filter_s[l][1]
                windows_dic[char] -= 1
                start, end = filter_s[l][0], filter_s[r][0]
                if end - start +1 < res[0]:
                    res = end - start + 1, start, end
                if char in dic and windows_dic[char] < dic[char]:
                    formed -= 1
                l += 1
            r += 1
        return "" if res[0] == float("inf") else s[res[1]:res[2]+1]





if __name__ == '__main__':
    string = "ADOBECODEBANC"
    t = "ABC"
    s = Solution()
    print(s.minWindow2(string, t))






