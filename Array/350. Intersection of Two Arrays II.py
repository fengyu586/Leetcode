# -*- coding: utf-8 -*-
# @Author  : Jing
# @FileName: 350. Intersection of Two Arrays II.py
# @IDE: PyCharm
# https://leetcode.com/problems/intersection-of-two-arrays-ii/


class Solution:
    def intersect(self, nums1, nums2):
        res = []
        if not nums1 or not nums2:
            return res
        dic = {}
        for num in nums1:
            dic[num] = dic.get(num, 0) + 1
        for num in nums2:
            if num in dic and dic[num] > 0:
                res.append(num)
                dic[num] -= 1
        return res


if __name__ == '__main__':
    nums1, nums2 = [4, 9, 5], [9, 4, 9, 8, 4]
    s = Solution()
    print(s.intersect(nums1, nums2))


