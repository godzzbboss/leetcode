#!/bin/python
# -*- coding: utf8 -*-
import sys
import os
import re


# 请完成下面这个函数，实现题目要求的功能
# 当然，你也可以不按照下面这个模板来作答，完全按照自己的想法来 ^-^
# ******************************开始写代码******************************
max_len = 0
cur_len = 0
_matrix_rows = 0
_matrix_cols = 0
_matrix_rows = int(input())
_matrix_cols = int(input())
_matrix = []
for _matrix_i in range(_matrix_rows):
    _matrix_temp = map(int, re.split(r'\s+', input().strip()))
    _matrix.append(_matrix_temp)

def longpath(matrix):
    global cur_len, max_len
    if not matrix or not matrix[0]:
        return 0
    rows = len(matrix)
    cols = len(matrix[0])
    for i in range(rows):
        for j in range(cols):
            cur_len = 0
            get_long_path(matrix, i ,j)

    return max_len
def get_long_path(matrix, row, col):
    cur = matrix[row][col]
    global cur_len, max_len
    cur_len += 1
    if cur_len > max_len:
        max_len = cur_len
    if col + 1 < _matrix_cols and matrix[row][col+1] > cur:
        get_long_path(matrix, row, col + 1)
    if col - 1 >= 0 and matrix[row][col-1] > cur:
        get_long_path(matrix, row, col - 1)
    if row + 1 < _matrix_rows and matrix[row+1][col] > cur:
        get_long_path(matrix, row + 1, col)
    if row - 1 >= 0 and matrix[row-1][col] > cur:
        get_long_path(matrix, row - 1, col)
    matrix[row][col] = cur
    cur_len -= 1





# ******************************结束写代码******************************
res = longpath(_matrix)

print(str(res) + "\n")