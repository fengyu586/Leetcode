# -*- coding: utf-8 -*-
# @Author  : Jing
# @FileName: 57.1和为s的连续正数序列.py
# @IDE: PyCharm


class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        if tsum <= 0:
            return 0
        left, right = (tsum)//2, (tsum)//2+1
        res = []
        while left != 0:
            if right - left == 1:
                cur_sum = left+right
            else:
                cur_sum = (right-left+1)*(right+left)/2
            if cur_sum == tsum:
                res.append([i for i in range(left, right+1)])
                right -= 1
                left -= 1
            elif cur_sum > tsum:
                right -= 1
                left -= 1
            else:
                left -= 1
        return sorted(res, key=lambda x:x[0])

    def FindContinuousSequence2(self, tsum):
        if tsum <= 0:
            return 0
        left, right = 1, 2
        max_val = tsum//2+1
        res = []
        while right <= max_val:
            if right - left == 1:
                cur_sum = left + right
            else:
                cur_sum = (right - left + 1) * (right + left) / 2
            if cur_sum == tsum:
                res.append([i for i in range(left, right+1)])
                right += 1
            elif cur_sum > tsum:
                left += 1
            else:
                right += 1
        return res


if __name__ == '__main__':
    tsum = 100
    s = Solution()
    print(s.FindContinuousSequence2(tsum))
