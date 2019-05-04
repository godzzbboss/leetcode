# -*- coding: utf-8 -*-

"""
__author__ == "BigBrother"

"""


class Solution:
    def test(self, input, filter, padding, stride):
        """input为输入矩阵，filter为卷积核，返回卷积之后的结果"""
        if padding:
            for item in input:
                item.insert(0,0)
                item.append(0)
            z = [0] * len(input[0])
            input.insert(0, z)
            input.append(z)
        i_h = len(input)
        i_w = len(input[0])
        f_h = len(filter)
        f_w = len(filter[0])
        # 保证（n+2p-f）% s == 0
        if (i_h - f_h) % stride != 0:
            print("!!请重新分配padding的长度")
            return
        if (i_w - f_w) % stride != 0:
            print("请重新分配padding的长度")
            return
        res = []
        for i in range(0, i_h - f_h + stride, stride): # 行
            sub_res = []
            for j in range(0, i_w - f_w + stride, stride): # 列
                sub_res.append(self.sum(input, i, j, filter))
            res.append(sub_res)
        return res


    def sum(self, input, row, col, filter):
        """row,col为卷积操作在input的起始位置"""
        f_h = len(filter)
        f_w = len(filter[0])
        res = 0
        for i in range(0, f_h):
            for j in range(0, f_w):
               res += input[row+i][col+j] * filter[i][j]

        return res



if __name__ == "__main__":
    s = Solution()
    input = [[1,1,1,0,0],[0,1,1,1,0], [0,0,1,1,1],[0,0,1,1,0],[0,1,1,0,0]]
    filter = [[1,0,1],[0,1,0],[1,0,1]]

    print(s.test(input, filter, 0, 2))