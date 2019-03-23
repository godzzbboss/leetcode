# -*- coding: utf-8 -*-

"""
__author__ = "BigBrother"

"""


class Solution():
    def test(self, array):
        if len(array) == 0:
            return 0
        if array[-1] > array[0]: # 本身有序
            return array[0]
        l = 0
        r = len(array) - 1
        while l < r:
            mid = (l + r) // 2
            if array[mid] > array[0]:
                l = mid + 1
            else:
                r = mid

        return array[l]


if __name__ == "__main__":
    s = Solution()
    print(s.test())

