# -*- coding: utf-8 -*-
# @Author  : Jing
# @FileName: 47. Permutations II.py
# @IDE: PyCharm
# https://leetcode.com/problems/permutations-ii/
# Solution 1: recursion
# Solution 2: dfs+cut
# Solution 3: dfs+cut best


class Solution:
    def __init__(self):
        self.res = []

    def generate(self, nums, index):
        if index == len(nums) and nums not in self.res:
            self.res.append([i for i in nums])
            return
        for i in range(index, len(nums)):
            nums[index], nums[i] = nums[i], nums[index]
            self.generate(nums, index + 1)
            nums[index], nums[i] = nums[i], nums[index]

    def permuteUnique1(self, nums):
        if not nums:
            return nums
        self.generate(nums, 0)
        return self.res

    def generate1(self, nums, cur):
        if len(nums) == 1 and cur+nums not in self.res:
            self.res.append(cur+nums)
            return
        for i in range(len(nums)):
            new_nums = nums[:i]+nums[i+1:]
            self.generate1(new_nums, cur+[nums[i]])

    def permuteUnique2(self, nums):
        if not nums:
            return nums
        self.generate1(nums, [])
        return self.res

    def dfs(self, nums, visited, path, res):
        if len(nums) == len(path):
            res.append([i for i in path])
            return
        for i in range(len(nums)):
            if not visited[i]:
                if i > 0 and visited[i-1] and nums[i] == nums[i-1]:
                    continue
                visited[i] = True
                self.dfs(nums, visited, path+[nums[i]], res)
                visited[i] = False


    def permuteUnique3(self, nums):
        if not nums:
            return nums
        path, res = [], []
        visited = [False for _ in range(len(nums))]
        nums = sorted(nums)
        self.dfs(nums, visited, path, res)
        return res



if __name__ == '__main__':
    nums = [1, 1, 2]
    s = Solution()
    print(s.permuteUnique3(nums))


