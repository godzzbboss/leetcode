# -*- coding: utf-8 -*-

"""
__author__ = "BigBrother"

"""


class Solution():
    def test(self, matrix):
        if not matrix:
            return []

        top_r = 0 # 左上角的行号
        top_c = 0 # 左上角的列号
        down_r = len(matrix) - 1 # 右下角的行号
        down_c = len(matrix[0]) - 1 # 右下角的列号
        result = []
        while top_r <= down_r and top_c <= down_c:
            self.print_matrix(matrix, top_r, top_c, down_r, down_c, result)
            top_r += 1
            top_c += 1
            down_r -= 1
            down_c -= 1

        return result


    def print_matrix(self, matrix, top_r, top_c, down_r, down_c, result):
        """顺时针打印矩阵的一圈"""
        cur_r = top_r # 当前遍历到的行标
        cur_c = top_c # 当前遍历到的列表

        if top_r == down_r: # 如果只有一行
            while cur_c <= down_c:
                result.append(matrix[top_r][cur_c])
                cur_c += 1

        elif top_c == down_c: # 如果只有一列
            while cur_r <= down_r:
                result.append(matrix[cur_r][top_c])
                cur_r += 1

        else: # 顺时针打印一圈
            while cur_c < down_c: # 从左往右打印
                result.append(matrix[cur_r][cur_c])
                cur_c += 1

            while cur_r < down_r: # 从上往下打印
                result.append(matrix[cur_r][cur_c])
                cur_r += 1

            while cur_c > top_c: # 从右往左遍历
                result.append(matrix[cur_r][cur_c])
                cur_c -= 1

            while cur_r > top_r: # 从下往上遍历
                result.append(matrix[cur_r][cur_c])
                cur_r -= 1

if __name__ == "__main__":
    s = Solution()
    print(s.test())

