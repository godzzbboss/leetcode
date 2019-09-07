# -*- coding: utf-8 -*-

"""
__author__ == "BigBrother"

"""

"""
    用BFS来做
"""
n, m = list(map(int, input().split()))
g = []
for i in range(n):
    row = list(map(int, input().split()))
    g.append(row)

d = [[-1]*m for i in range(n)] # 初始化每个点到左上角起始点的距离
flag =  [[False]*m for i in range(n)]# 记录每个点是否访问过
q = []

q.append([0,0]) # 头节点入队, 每个点用其下标表示
d[0][0] = 0
flag[0][0] = True
dx = [1, -1, 0, 0] # 下，上，左，右四个方向
dy = [0, 0, -1, 1]
while q:
    t = q.pop(0) # 头节点出队
    for i in range(4): # 对于每个点来说有四个方向可以走
        # 当前点的下一个点
        x_ = t[0] + dx[i]
        y_ = t[1] + dy[i]
        if x_ >= 0 and x_ <= n-1 and y_ >= 0 and y_ <= m-1 and not flag[x_][y_]:
            if g[x_][y_] == 0: # 可以走
                q.append([x_, y_])
                d[x_][y_] = d[t[0]][t[1]] + 1
                flag[x_][y_] = True
print(d[n-1][m-1])


