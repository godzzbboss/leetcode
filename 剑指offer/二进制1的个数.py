# -*- coding: utf-8 -*-

"""
__author__ = "BigBrother"

"""


class Solution:
    def NumberOf1(self, n):
        # write code here
        n = n & 0xffffffff # 将n转为无符号整数
        count = 0
        while n: # 在python中，整数的位数并不是32位，所以自己限定一下
            if n & 1 == 1:
                count += 1
            n = n >> 1
        return count

