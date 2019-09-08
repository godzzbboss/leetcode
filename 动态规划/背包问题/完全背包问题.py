# -*- coding: utf-8 -*-

"""
__author__ == "BigBrother"

"""
"""
有 N 种物品和一个容量是 V 的背包，每种物品都有无限件可用。

第 i 种物品的体积是 vi，价值是 wi。

求解将哪些物品装入背包，可使这些物品的总体积不超过背包容量，且总价值最大。
输出最大价值。
输入样例
4 5
1 2
2 4
3 4
4 5
输出样例：
10

"""


# N, V = list(map(int, input().split()))

# v = [0] * 1010
# w = [0] * 1010

# f = [[0] * 1010 for i in range(1010)]

# for i in range(1, N+1):
#     v_, w_ = list(map(int, input().split()))
#     v[i] = v_
#     w[i] = w_

# for i in range(1, N+1):
#     for j in range(V+1):
#         if v[i] > j:
#             f[i][j] = f[i-1][j]
#         else:
#             f[i][j] = max(f[i-1][j], f[i][j-v[i]] + w[i])
# print(f[N][V])

"""
1维优化
"""

N, V = list(map(int, input().split()))

v = [0] * 1010
w = [0] * 1010

f = [0] * 1010

for i in range(1, N+1):
    v_, w_ = list(map(int, input().split()))
    v[i] = v_
    w[i] = w_

for i in range(1, N+1):
    for j in range(v[i], V+1):
        f[j] = max(f[j], f[j-v[i]] + w[i])
print(f[V])