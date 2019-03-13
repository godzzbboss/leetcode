# -*- coding: utf-8 -*-

"""
__author__ = "BigBrother"

"""


class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        if len(array) == 0 or len(array[0]) == 0:
            return False
        row_nums = len(array)
        col_nums = len(array[0])
        row = 0
        col = col_nums - 1
        while row <= row_nums - 1 and col >= 0:
            if array[row][col] == target:
                return True
            elif array[row][col] < target:
                row += 1
            else:
                col -= 1
        return False

if __name__ == "__main__":
    s = Solution()
    target = 1
    array = [[1,2,3],[4,5,6]]
    print(s.Find(target, array))