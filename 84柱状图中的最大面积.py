# -*- coding: utf-8 -*-

"""
__author__ == "BigBrother"

"""


class Solution:

    """
        找到每个数左边和右边离它最近且比它小的数
        这种方法可以求出以每个数为轴的最大面积

    """
    # def largestRectangleArea(self, heights):
    #     if not heights:
    #         return 0
    #     # 找到每个数左边离它最近的比它小的数
    #     stack1 = []  # 保存每个数及其相应的位置
    #     res1 = [-1] * len(heights)
    #     for i in range(len(heights)):
    #         while stack1 and heights[i] <= stack1[-1][1]:
    #             stack1.pop()
    #         if stack1:
    #             res1[i] = stack1[-1][0]
    #         # 如果栈为空，则说明该元素左边没有比它小的数，位置设为-1
    #         stack1.append((i, heights[i]))
    #
    #     # 找到每个数右边离它最近比它小的数
    #     stack2 = []  # 保存每个数及其相应的位置
    #     res2 = [len(heights)] * len(heights)
    #     for i in range(len(heights)):
    #         while stack2 and heights[i] < stack2[-1][1]:
    #             res2[stack2[-1][0]] = i
    #             stack2.pop()
    #         stack2.append((i, heights[i]))
    #     # 找到最大面积
    #     max_area = 0
    #     for i in range(len(heights)):
    #         max_area = max(max_area, heights[i] * (res2[i] - res1[i] - 1))
    #
    #     return max_area

    """
        维护一个单增栈，找到每个数左边和右边离它最近的比它小的数的位置
    """
    def largestRectangleArea(self, heights):
        if not heights:
            return 0
        heights.append(-1)
        stack = [] # 保存的是每个元素的下标
        max_area = 0
        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                t = stack.pop() # t右边离它最近且比它小的数就是当前元素
                if stack:
                    max_area = max(max_area, heights[t] * (i - stack[-1] - 1)) # t出栈之后，t左边离他最近且比他小的数就是栈顶元素
                else:
                    max_area = max(max_area, heights[t] * (i - (-1) - 1))
            stack.append(i)

        return max_area



s = Solution()
a = [2,1,2]
print(s.largestRectangleArea(a))
