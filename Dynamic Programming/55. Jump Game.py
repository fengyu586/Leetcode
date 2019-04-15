#!/usr/bin/python3.6
# -*- coding:utf-8 -*-
# https://leetcode.com/problems/jump-game/


class Solution:
    def canJump(self, nums):
        n = len(nums)
        goal = n - 1
        for i in range(n - 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return not (goal)


def main():
    s = Solution()
    li = [2, 3, 1, 1, 4]
    print(s.canJump(li))


if __name__ == '__main__':
    main()


