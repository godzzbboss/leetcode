# -*- coding: utf-8 -*-

"""
__author__ = "BigBrother"

"""

import copy
from collections import deque


class Solution():

    def __init__(self):
        self.result = []

    def test(self, nums, start, end):
        self.perm(nums, start, end)
        final_result = []
        for i in range(len(self.result)):
            final_result.append(self.result[i][start:end+1])
        return final_result


    def perm(self, nums, start, end):
        """

        :param nums:
        :param start:
        :param end:
        :return:
        """

        if start == end: # 全排列完成或者只有一个元素
            _ = []
            for i in range(0, end+1): # 虽然是对指定部分做全排列，但是还是要全部分返回
                _.append(nums[i])
            self.result.append(_)

        for i in range(start, end+1):
            nums[i], nums[start] = nums[start], nums[i]
            self.perm(nums, start+1, end)
            nums[i], nums[start] = nums[start], nums[i]


    # 用队列实现全排列
    from collections import deque
    # def permut(self, nums):
    #     if not nums:
    #         return [[]]
    #     d = deque([[]])
    #     while 1:
    #         if len(d[0]) == len(nums): #完成全排列
    #             break
    #         temp = d.popleft()
    #         for val in nums:
    #             if val in temp:
    #                 continue
    #             else:
    #                 d.append(temp + [val])
    #     return list(d)






if __name__ == "__main__":
    s = Solution()
    nums = ["a", "b", "c", "d"]
    # a = s.permut(nums)
    a = s.test(nums, 1, len(nums) - 1)
    print(a)