# -*- coding: utf-8 -*-

"""
__author__ = "BigBrother"

"""


class Solution():
    def test(self, threshold, rows, cols):
        flag = [[False] * cols for _ in range(rows)]
        return self.get_result(threshold, rows, cols, 0, 0, flag)


    def get_result(self, threshold, rows, cols, i, j, flag):
        """判断（i，j）是否可以进入"""
        if i < 0 or j < 0 or i >= rows or j >= cols:
            return 0
        if self.transform(i) + self.transform(j) > threshold:
            return 0

        # 可以进入
        if self.transform(i) + self.transform(j) <= threshold and flag[i][j] == False:
            flag[i][j] = True
            # 判断其周围的元素
            return 1 + self.get_result(threshold, rows, cols, i-1, j , flag) + self.get_result(threshold, rows, cols, i+1, j , flag) + self.get_result(
                threshold, rows, cols, i, j-1, flag) + self.get_result(threshold, rows, cols, i, j+1 , flag)
        return 0

    def transform(self, num):
        """将一个数转为各个位相乘"""
        sum = 0
        while num:
            sum += num % 10 # 取个位数
            num = num //10

        return sum



if __name__ == "__main__":
    s = Solution()
    print(s.test())

