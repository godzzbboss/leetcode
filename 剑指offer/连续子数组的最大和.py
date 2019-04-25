# -*- coding: utf-8 -*-

"""
__author__ == "BigBrother"

"""

import sys
class Solution:
    def test(self, array):
        if not array:
            return 0
        cur_sum = array[0]
        max_sum = - sys.maxsize
        for i in range(1, len(array)):
            if cur_sum < 0:
                cur_sum = array[i]
            else:
                cur_sum += array[i]
            if max_sum < cur_sum:
                max_sum = cur_sum
        return max_sum

if __name__ == "__main__":
    pass