# -*- coding: utf-8 -*-

"""
__author__ = "BigBrother"

"""


class Solution:
    def generate(self, numRows):
        if numRows == 0:
            return []

        result = []
        for i in range(numRows):  # 共 numRows行
            sub_result = []
            if i == 0:
                sub_result.append(1)
                result.append(sub_result)
            else:
                for j in range(i+1):  # 生成每一行的数据
                    if j == 0 or j == i:
                        sub_result.append(1)
                    else:
                        sub_result.append(result[i - 1][j - 1] + result[i - 1][j])
                result.append(sub_result)

        return result


if __name__ == "__main__":
    s = Solution()
    print(s.generate(3))

