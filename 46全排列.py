# -*- coding: utf-8 -*-

"""
__author__ = "BigBrother"

"""

import copy
from collections import deque


class Solution():
    # def __init__(self):
    #     self.results = []
    # def test(self, nums):
    #     self.perm(nums, 0, len(nums)-1)
    #     return self.results
    #
    #
    # def perm(self, nums, position, end):
    #     if position == end:
    #         temp = copy.deepcopy(nums) # 这个地方是关键，在递归过程中nums指向的内存区域被共享，递归返回上层是会影响已经存储的nums值，因此用深拷贝
    #         self.results.append(temp)
    #     else:
    #         for index in range(position, end + 1):
    #             nums[index], nums[position] = nums[position], nums[index]
    #             self.perm(nums, position + 1, end)
    #             nums[index], nums[position] = nums[position], nums[index]


    # 用队列实现全排列
    from collections import deque
    def permut(self, nums):
        if not nums:
            return [[]]
        d = deque([[]])
        while 1:
            if len(d[0]) == len(nums): #完成全排列
                break
            temp = d.popleft()
            for val in nums:
                if val in temp:
                    continue
                else:
                    d.append(temp + [val])
        return list(d)






if __name__ == "__main__":
    s = Solution()
    nums = ["a", "b", "c"]
    a = s.permut(nums)
    print(a)