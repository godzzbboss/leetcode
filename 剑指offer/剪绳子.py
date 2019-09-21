# -*- coding: utf-8 -*-

"""
__author__ == "BigBrother"

"""
class Solution(object):
    def maxProductAfterCutting(self,length):
        """
        :type length: int
        :rtype: int
        """
        f = [0] * (length + 10) # f[i]表示将长度为i的绳子剪成多段的最大乘积
        f[0] = 0
        f[1] = 0
        f[2] = 1
        f[3] = 2
        for i in range(4, length+1):
            for j in range(1, i): # 第一段的长度
               f[i] = max(f[i], j*(i-j), j*f[i-j])

        print(f[length])
s = Solution()
s.maxProductAfterCutting(8)

