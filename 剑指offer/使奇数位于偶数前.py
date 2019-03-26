# -*- coding: utf-8 -*-

"""
__author__ = "BigBrother"

"""


class Solution():
    # def test(self, array):
    #     """头尾双指针会使数组的元素相对位置发生改变"""
    #     if len(array) == 0:
    #         return
    #     l = 0
    #     r = len(array) - 1
    #     while l < r:
    #         while array[l] & 1 == 1: # 奇数
    #             l += 1
    #         while array[r] & 1 == 0: # 偶数
    #             r -= 1
    #         if l < r:
    #             array[l], array[r] = array[r], array[l]
    #
    #     return array

    def test(self, array):
        """空间换时间"""
        odd = []
        even = []
        for i in range(len(array)):
            if array[i] & 1 == 1:
                odd.append(array[i])
            else:
                even.append(array[i])
        return odd + even




if __name__ == "__main__":
    s = Solution()
    array = [1,3,4,2,6]
    print(s.test(array))

