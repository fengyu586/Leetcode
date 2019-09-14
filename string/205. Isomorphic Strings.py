# -*- coding: utf-8 -*-
# @Author  : Jing
# @FileName: 205. Isomorphic Strings.py
# @IDE: PyCharm
# https://leetcode.com/problems/isomorphic-strings/


class Solution:
    def isIsomorphic(self, s, t):
        if len(set(s)) != len(set(t)):
            return False
        n = len(s)
        s_dic, t_dic = {}, {}
        for i in range(n):
            if s[i] not in s_dic:
                s_dic[s[i]] = t[i]
            if t[i] not in t_dic:
                t_dic[t[i]] = s[i]
            if s_dic[s[i]] == t[i] and t_dic[t[i]] == s[i]:
                continue
            else:
                return False
        return True


if __name__ == '__main__':
    S = Solution()
    s, t = 'egg', 'add'
    print(S.isIsomorphic(s, t))             # Output is True



