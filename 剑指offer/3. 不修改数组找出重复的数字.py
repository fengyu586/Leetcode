# -*- coding: utf-8 -*-
# @Author  : Jing
# @FileName: 3. 不修改数组找出重复的数字.py
# @IDE: PyCharm
# 3. 数组中重复的数字变种


class Solution:
    def count_range(self, nums, start, end):
        if nums is None or len(nums) == 0:
            return 0
        count = 0
        for i in nums:
            if start <= i and i <= end:
                count += 1
        return count

    def duplicate(self, nums):
        if 0 in nums:
            return None
        if nums is None:
            return None
        if len(nums) == 0:
            return None
        n = len(nums)
        start = 1
        end = n-1
        while end >= start:
            mid = ((end-start) >> 1)+start
            count = self.count_range(nums, start, mid)
            if end == start:
                if count > 1:
                    return start
                else:
                    break
            if count > (mid-start+1):
                end = mid
            else:
                start = mid + 1
        return None



if __name__ == '__main__':
    nums = [2, 3, 5, 4, 3, 2, 6, 7]
    s = Solution()
    print(s.duplicate(nums))

