# -*- coding: utf-8 -*-

"""
__author__ = "BigBrother"

"""


class Solution(object):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    def hasPath(self, matrix, string):
        """
        :type matrix: List[List[str]]
        :type string: str
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        rows = len(matrix)
        cols = len(matrix[0])
        flag = [[False] * cols for i in range(rows)]

        for i in range(rows):
            for j in range(cols):
                if self.dfs(matrix, rows, cols, i, j, string, 0, flag):
                    return True
        return False

    def dfs(self, matrix, rows, cols, i, j, string, k, flag):

        if i < 0 or i >= rows or j < 0 or j >= cols:
            return False
        if matrix[i][j] != string[k] or flag[i][j] == True:
            return False
        if k == len(string) - 1 and matrix[i][j] == string[k]:
            return True

        flag[i][j] = True  # 遍历该点
        bool_f = False
        for idx in range(4):
            i_ = i + self.dx[idx]
            j_ = j + self.dy[idx]
            bool_f = bool_f or self.dfs(matrix, rows, cols, i_, j_, string, k + 1, flag)
        flag[i][j] = False  # 恢复现场
        if bool_f:
            return True  # 从该点遍历能找到一条路径
        return False

if __name__ == "__main__":
    s = Solution()
    print(s.test())

