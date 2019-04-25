# -*- coding: utf-8 -*-

"""
__author__ == "BigBrother"

"""


class Solution:
    # def test(self, matrix):
    #     if not matrix or not matrix[0]:
    #         return 0
    #     rows = len(matrix)
    #     cols = len(matrix[0])
    #     ids_matrix = [[False] * cols for i in range(rows)] # 记录元素是否访问过
    #     max_len = 0
    #     for i in range(rows):
    #         for j in range(cols):
    #             c = self.get_longest_path(matrix, rows, cols, i, j, ids_matrix)
    #             max_len = max(max_len, c)
    #
    #     return max_len
    #
    # def get_longest_path(self, matrix, rows, cols, i, j, ids_matrix):
    #     """返回从matrix[i][j]开始寻找的最长递增路径长度"""
    #     if i < 0 or j < 0 or i >= rows or j >= cols:
    #         return 0
    #     if ids_matrix[i][j] == True:
    #         return 0
    #     cur = matrix[i][j]
    #     ids_matrix[i][j] = True
    #     res = 0
    #     if i > 0 and matrix[i -1][j] > cur:
    #         res = max(res, self.get_longest_path(matrix, rows, cols, i-1, j, ids_matrix) + 1)
    #     if i+1 < rows and matrix[i+1] > cur:
    #         res = max(res, self.get_longest_path(matrix, rows, cols, i + 1, j, ids_matrix) + 1)
    #     if j > 0 and matrix[i][j-1] > cur:
    #         res = max(res, self.get_longest_path(matrix, rows, cols, i, j-1, ids_matrix) + 1)
    #     if j+1 < cols and matrix[i][j + 1] > cur:
    #         res = max(res, self.get_longest_path(matrix, rows, cols, i, j+1, ids_matrix) + 1)
    #     ids_matrix[i][j] = False
    #     return res


    """
        上述写法超时了，与其用一个矩阵标志每个元素是否搜索过，不妨设置一个矩阵保存从当前位置开始能搜索到的最长递增路径的长度，
        这样既可以标志当前位置是否搜索过，又能重复利用已经知道的信息，减少时间复杂度
    """
    def test(self, matrix):
        if not matrix or not matrix[0]:
            return 0
        rows = len(matrix)
        cols = len(matrix[0])
        max_path_len = 0
        counts = [[0] * cols for _ in range(rows)] # 记录从每个位置出发的最长递增路径长度
        # 从所有可能的出发点开始搜索
        for i in range(rows):
            for j in range(cols):
                max_path_len = max(max_path_len, self.get_longest_path(matrix, rows, cols, i, j, counts))
        return max_path_len

    def get_longest_path(self, matrix, rows, cols, i, j, counts):
        """返回从i,j位置开始寻找的最长递增序列长度"""
        if counts[i][j]:
            return counts[i][j]
        cur = matrix[i][j]
        max_len = 1

        if i > 0 and matrix[i-1][j] > cur:
            max_len = max(max_len, self.get_longest_path(matrix, rows, cols, i-1, j, counts) + 1)
        if i + 1 < rows and matrix[i+1][j] > cur:
            max_len = max(max_len, self.get_longest_path(matrix, rows, cols, i+1, j, counts) + 1)
        if j > 0 and matrix[i][j-1] > cur:
            max_len = max(max_len, self.get_longest_path(matrix, rows, cols, i, j-1, counts) + 1)
        if j+1 < cols and matrix[i][j+1] > cur:
            max_len = max(max_len, self.get_longest_path(matrix, rows, cols, i, j+1, counts) + 1)
        counts[i][j] = max_len

        return max_len


if __name__ == "__main__":
    pass