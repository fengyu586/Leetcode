# -*- coding: utf-8 -*-
# @Author  : Jing
# @FileName: 71. Simplify Path.py
# @IDE: PyCharm
# https://leetcode.com/problems/simplify-path/
# Solution: O(n)Time O(n)Space


class Solution:
    def simplifyPath(self, path):
        if not path:
            return ""
        stack = []
        string = path.split("/")
        for p in string:
            if stack and p == "..":
                stack.pop()
            elif p != "" and p != "." and p != "..":
                stack.append(p)
        return "/"+"/".join(stack)


if __name__ == '__main__':
    path = "/a/./b/../../c/"
    s = Solution()
    print(s.simplifyPath(path))


