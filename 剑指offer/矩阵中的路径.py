# -*- coding: utf-8 -*-

"""
__author__ = "BigBrother"

"""


class Solution():

    def test(self, matrix, rows, cols, s):
        flag = [False] * len(matrix)
        if len(matrix) == 0:
            return False
        if len(s) == 0:
            return True
        for i in range(rows):
            for j in range(cols):
                if self.is_has_path(matrix, rows, cols, i, j, s, 0, flag):
                    return True
        return False


    def is_has_path(self, matrix, rows, cols, i, j, s, k, flag):
        if i < 0 or j < 0 or i >= rows or j >= cols:
            return False
        index = i * cols + j

        if matrix[index] != s[k] or flag[index] == True:
            return False

        if k == len(s) - 1:
            return True

        flag[index] = True

        # 从 index 周围的四个格子中继续找路径
        if self.is_has_path(matrix, rows, cols, i-1, j, s, k+1) or \
            self.is_has_path(matrix, rows, cols, i+1, j, s, k + 1) or\
            self.is_has_path(matrix, rows, cols, i, j-1, s, k + 1) or\
            self.is_has_path(matrix, rows, cols, i, j+1, s, k + 1):

            return True

        # 没找到，说明从index这个位置开始找，找不到路径，将flag设为False
        flag[index] = False

        return False







if __name__ == "__main__":
    s = Solution()
    print(s.test())

