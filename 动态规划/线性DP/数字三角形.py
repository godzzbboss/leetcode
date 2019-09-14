# -*- coding: utf-8 -*-

"""
__author__ == "BigBrother"

"""
"""
 给定一个如下图所示的数字三角形，从顶部出发，在每一结点可以选择移动至其左下方的结点或移动至其右下方的结点，一直走到底层，要求找出一条路径，使路径上的数字的和最大。

        7
      3   8
    8   1   0
  2   7   4   4
4   5   2   6   5
输入格式
第一行包含整数n，表示数字三角形的层数。

接下来n行，每行包含若干整数，其中第 i 行表示数字三角形第 i 层包含的整数。

输出格式
输出一个整数，表示最大的路径数字和。

数据范围
1≤n≤500,
−10000≤三角形中的整数≤10000 
输入样例：
5
7
3 8
8 1 0 
2 7 4 4
4 5 2 6 5
输出样例：
30
"""
# 二维DP
n = int(input())
N = 510
g = [[0] * N for i in range(N)]
f = [[-11111] * N for i in range(N)]

for i in range(1, n + 1):
    cols = list(map(int, input().split()))
    for j in range(1, len(cols) + 1):
        g[i][j] = cols[j - 1]
f[1][1] = g[1][1]
for i in range(2, n+1):
    for j in range(1, i+1):
        f[i][j] = max(f[i-1][j-1], f[i-1][j]) + g[i][j]
res = -11111
for i in range(1, n+1):
    res = max(res, f[n][i])
print(res)

# 一维DP
n = int(input())
N = 510
g = [[0] * N for i in range(N)]
f = [-11111] * N

for i in range(1, n + 1):
    cols = list(map(int, input().split()))
    for j in range(1, len(cols) + 1):
        g[i][j] = cols[j - 1]
f[1] = g[1][1]
for i in range(2, n+1):
    for j in range(i, 0, -1):
        f[j] = max(f[j-1], f[j]) + g[i][j]
res = -11111
for i in range(1, n+1):
    res = max(res, f[i])
print(res)
