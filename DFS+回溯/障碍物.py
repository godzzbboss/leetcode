# -*- coding: utf-8 -*-

"""
__author__ == "BigBrother"

"""

"""
题目描述：
你现在在(0,0)，需要到(x,y)去，路上有n个障碍物。给出每个障碍物的坐标，你只能平行于坐标轴走整数步，问你最少需要多少步才能走到目的地。

输入
第一行三个数x,y,n

接下来n行，每行描述一个障碍物的坐标x_i,y_i

-500≤x,y,x_i,y_i≤500

n≤10000

保证有解
输出
输出一个数，代表最少的步数。


样例输入
2 0 3
1 0
1 1
1 -1
样例输出
6
"""
x, y, n = list(map(int, input().split()))
N = 500
g = [[0] * 1001 for i in range(1001)]
d = [[-1] * 1001 for i in range(1001)] # 保存每个点到起点的最小距离
for i in range(n):
    x_, y_ = list(map(int, input().split()))
    g[x_+N][y_+N] = 1

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs():
    q = []
    d[N][N] = 0
    q.append((N, N))
    while q:
        t = q[0] # 队头
        q.pop(0)
        for i in range(4):
            x_ = t[0] + dx[i]
            y_ = t[1] + dy[i]
            if x_ >= 0 and x_ <= 1000 and y_ >= 0 and y_ <= 1000 and g[x_][y_] == 0 and d[x_][y_] == -1:
                d[x_][y_] = d[t[0]][t[1]] + 1
                if x_ == x + N and y_ == y + N:
                    return d[x_][y_]
                q.append((x_, y_))
    return d[x+N][y+N]

print(bfs())

