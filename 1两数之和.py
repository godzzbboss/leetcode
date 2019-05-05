# -*- coding: utf-8 -*-

"""
__author__ == "BigBrother"

"""


class Solution:
    def test(self, nums, target):
        """给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标"""
        if not nums:
            return []
        d = {}
        for ids, num in enumerate(nums):
            left = target - num
            if left in d:
                return [d[left], ids]
            else:
                d[num] = ids
if __name__ == "__main__":
    pass