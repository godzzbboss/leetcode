# -*- coding: utf-8 -*-

"""
__author__ == "BigBrother"

"""


class Solution:
    def test(self, array, num):
        """num在排序数组array中出现的次数"""
        if not array:
            return 0
        first = self.binary_search_first(array, num)
        last = self.binary_search_last(array, num)
        if first == last and array[first] != num: # 说明数组中不存在num
            return 0

        return last - first + 1

    def binary_search_first(self, array, num):
        """num在排序数组中第一次出现的位置"""
        left = 0
        right = len(array) - 1
        while left < right:
            mid = (left + right) // 2
            if array[mid] >= num:
                right = mid
            else:
                left = mid + 1
        return left
    def binary_search_last(self, array, num):
        """num在排序数组array中最后出现的位置"""
        left = 0
        right = len(array) - 1
        while left < right:
            mid = (left + right + 1) // 2
            if array[mid] <= num:
                left = mid
            else:
                right = mid - 1
        return left




if __name__ == "__main__":
    s = Solution()
    array = [1,2,2,2,2]
    print(s.test(array, 2))