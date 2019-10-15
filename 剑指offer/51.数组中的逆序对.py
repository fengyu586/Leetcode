# -*- coding: utf-8 -*-
# @Author  : Jing
# @FileName: 51.数组中的逆序对.py
# @IDE: PyCharm


class Solution:
    def InversePairsCore(self, copy, data, start, end):
        if start == end:
            copy[start] = data[start]
            return 0
        length = (end-start)//2
        left = self.InversePairsCore(data, copy, start, start+length)
        right = self.InversePairsCore(data, copy, start+length+1, end)
        i = start+length
        j = end
        p_copy = end
        count = 0
        while i >= start and j >= start+length+1:
            if data[i] > data[j]:
                copy[p_copy] = data[i]
                i -= 1
                count += j-start-length
            else:
                copy[p_copy] = data[j]
                j -= 1
            p_copy -= 1
        while i >= start:
            copy[p_copy] = data[i]
            i -= 1
            p_copy -= 1
        while j >= start+length+1:
            copy[p_copy] = data[j]
            j -= 1
            p_copy -= 1
        return left+right+count

    def InversePairs(self, data):
        if not data:
            return 0
        copy = [i for i in data]
        start, end = 0, len(data) - 1
        return self.InversePairsCore(copy, data, start, end) % 1000000007


if __name__ == '__main__':
    nums = [7, 5, 6, 4]
    s = Solution()
    print(s.InversePairs(nums))