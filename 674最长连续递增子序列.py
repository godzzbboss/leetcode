# -*- coding: utf-8 -*-

"""
__author__ == "BigBrother"

"""
"""
给定一个未经排序的整数数组，找到最长且连续的的递增序列。

示例 1:

输入: [1,3,5,4,7]
输出: 3
解释: 最长连续递增序列是 [1,3,5], 长度为3。
尽管 [1,3,5,7] 也是升序的子序列, 但它不是连续的，因为5和7在原数组里被4隔开。 
示例 2:

输入: [2,2,2,2,2]
输出: 1
解释: 最长连续递增序列是 [2], 长度为1。
注意：数组长度不会超过10000。

"""
class Solution:
    def findLengthOfLCIS(self, nums):
        if not nums: return 0
        f = [0] * 10010 # f[i] 表示以第i个字符结尾的连续序列
        l = len(nums)
        nums.insert(0, -999999999)
        for i in range(1, l+1):
            f[i] = 1
            if nums[i] > nums[i-1]:
                f[i] = max(f[i], f[i-1] + 1)

        return max(f)

if __name__ == "__main__":
    s = Solution()
    nums = [1,3,5,4,7]
    print(s.findLengthOfLCIS(nums))
