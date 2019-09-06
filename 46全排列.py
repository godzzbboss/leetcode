# -*- coding: utf-8 -*-

"""
__author__ = "BigBrother"

"""

import copy
from collections import deque


class Solution():
    res = []
    """dfs实现全排列"""
    def permute(self, nums):
        if not nums:
            return []
        flag = [False] * len(nums)
        self.dfs(nums, 0, flag, [])
        return self.res

    def dfs(self, nums, u, flag, path):
        """

        :param nums:
        :param u: 当前搜索到哪个位置
        :param flag: 记录每个数是否使用过
        :param path: 记录当前路径
        :return:
        """
        if u == len(nums): # 找到一个全排列
            self.res.append(path)
            return
        for i in range(len(nums)):
            if flag[i] == False:
                path_ = path.copy()
                path_.append(nums[i])
                flag[i] = True
                self.dfs(nums, u+1, flag, path_)
                flag[i] = False # 回溯时恢复现场

if __name__ == "__main__":
    s = Solution()
    nums = ["a", "b", "c", "d"]
    print(s.permute(nums))