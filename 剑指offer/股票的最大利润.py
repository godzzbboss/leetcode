# -*- coding: utf-8 -*-

"""
__author__ == "BigBrother"

"""


class Solution:
    def test(self, nums):
        if len(nums) <= 1:
            return 0
        min_ = nums[0]
        res = 0
        for i in range(1, len(nums)):
            res = max(res, nums[i] - min_)
            min_ = min(min_, nums[i])
        return res

if __name__ == "__main__":
    pass