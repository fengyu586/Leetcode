# -*- coding: utf-8 -*-
# @Author  : Jing
# @FileName: 49. Group Anagrams.py
# @IDE: PyCharm
# https://leetcode.com/problems/group-anagrams/
# Solution 1: classifier the array after sort.
# Only when string sorted is the same as other,
# they are group anagrams.
# O(NKlogK)Time O(NK)Space
# Solution 2: classifier by count.
# Only when the number of every char occur in string is the same as other,
# they are group anagrams.O(NK)Time O(NK)Space


class Solution:
    def groupAnagrams1(self, strs):
        if not strs:
            return strs
        dic = {}
        for s in strs:
            tmp_s = list(s)
            tmp_s = sorted(tmp_s)
            tmp_s = ''.join(tmp_s)
            if tmp_s not in dic :
                    dic[tmp_s] = [s]
            else:
                dic[tmp_s].append(s)
        res = []
        for val in dic.values():
                res.append(val)
        return res

    def groupAnagrams2(self, strs):
        if not strs:
            return strs
        dic = {}
        for string in strs:
            count = [0 for _ in range(26)]
            for s in string:
                count[ord(s)-ord('a')] += 1
            count = tuple(count)
            if count not in dic:
                dic[count] = [string]
            else:
                dic[count].append(string)
        res = []
        for li in dic.values():
            res.append(li)
        return res


if __name__ == '__main__':
    strings = ["eat", "tea", "tan", "ate", "nat", "bat"]
    s = Solution()
    print(s.groupAnagrams2(strings))




