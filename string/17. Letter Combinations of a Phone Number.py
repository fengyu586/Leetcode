# -*- coding: utf-8 -*-
# @Author  : Jing
# @FileName: 17. Letter Combinations of a Phone Number.py
# @IDE: PyCharm


class Solution:
    def get_str(self, digits, dic, path, res, index):
        if len(path) == len(digits):
            res.append(path)
            return
        if index >= len(digits):
            return
        digit = digits[index]
        if digit in dic:
            string = dic[digit]
            for s in string:
                self.get_str(digits, dic, path+s, res, index + 1)

    def letterCombinations(self, digits):
        if not digits:
            return None
        nums = list(map(str, range(2, 10)))
        alphas = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        dic = dict(zip(nums, alphas))
        res, index = [], 0
        path = ''
        self.get_str(digits, dic, path, res, index)
        return res


if __name__ == '__main__':
    string = '23'
    s = Solution()
    print(s.letterCombinations(string))

