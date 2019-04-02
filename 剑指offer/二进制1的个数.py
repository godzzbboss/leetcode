# -*- coding: utf-8 -*-

"""
__author__ = "BigBrother"

"""


class Solution:
    def NumberOf1(self, n):
        # write code here
        count = 0
        nums = 0 # 移位次数
        while n and nums < 32: # 在python中，整数的位数并不是32位，所以自己限定一下
            if n & 1 == 1:
                count += 1
            n = n >> 1
            nums += 1
        return count

import math
math.isclose()
