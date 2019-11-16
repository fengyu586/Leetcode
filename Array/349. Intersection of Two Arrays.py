# -*- coding: utf-8 -*-
# @Author  : Jing
# @FileName: 349. Intersection of Two Arrays.py
# @IDE: PyCharm
# https://leetcode.com/problems/intersection-of-two-arrays/


class Solution:
    def intersection(self, nums1, nums2):
        nums1, nums2 = list(set(nums1)), list(set(nums2))
        dic, res = {}, []
        if not nums1 or not nums2:
            return res
        for num in nums1:
            dic[num] = 1
        for num in nums2:
            if num in dic:
                res.append(num)
        return res


if __name__ == '__main__':
    nums1, nums2 = [1, 2, 2, 3], [2, 2]
    s = Solution()
    print(s.intersection(nums1, nums2))
