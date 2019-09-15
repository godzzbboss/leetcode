# -*- coding: utf-8 -*-

"""
__author__ == "BigBrother"

"""
class Solution:
    def maximalRectangle(self, matrix):
        if not matrix or not matrix[0]:
            return 0
        rows = len(matrix)
        cols = len(matrix[0])
        for i in range(rows):
            matrix[i].append("0")

        heights = [0] * (cols+1)
        heights.append(-1)
        res = 0
        for i in range(rows):
            stack = [] # 保存下标
            for j in range(cols+1):
                if matrix[i][j] == "1":
                    heights[j] += 1
                else:
                    heights[j] = 0
                while stack and heights[j] < heights[stack[-1]]:
                    t = stack.pop()
                    if stack:
                        res = max(res, heights[t] * (j - stack[-1] - 1))
                    else:
                        res = max(res, heights[t] * (j))

                stack.append(j)
        return res

if __name__ == "__main__":
    s = Solution()
    matrix = [
      ["1","0","1","0","0"],
      ["1","0","1","1","1"],
      ["1","1","1","1","1"],
      ["1","0","0","1","0"]
    ]

    print(s.maximalRectangle(matrix))
