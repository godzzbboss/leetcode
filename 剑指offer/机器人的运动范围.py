# -*- coding: utf-8 -*-

"""
__author__ = "BigBrother"

"""


class Solution():
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    def test(self, threshold, rows, cols):
        flag = [[False] * cols for _ in range(rows)]
        return self.dfs(threshold, rows, cols, 0, 0, flag)

    def dfs(self, threshold, rows, cols, i, j, flag):
        """返回从[i，j]开始移动所能到达的格子数"""
        if i < 0 or j < 0 or i >= rows or j >= cols:
            return 0
        if self.transform(i) + self.transform(j) > threshold or flag[i][j] == True:
            return 0
        # 可以进入
        flag[i][j] = True
        # 判断其周围的元素
        res = 0
        for k in range(4):
            x_ = i + self.dx[k]
            y_ = j + self.dy[k]
            res += self.dfs(threshold, rows, cols, x_, y_ , flag)
        return 1 + res

    def transform(self, num):
        """将一个数转为各个位相加"""
        sum = 0
        while num:
            sum += num % 10 # 取个位数
            num //= 10

        return sum

if __name__ == "__main__":
    s = Solution()
    print(s.test(7,4,5))

