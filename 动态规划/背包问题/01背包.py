# -*- coding: utf-8 -*-

"""
__author__ == "BigBrother"

"""
"""
01背包问题是没见物品只能装一次，求最大价值
有 N 件物品和一个容量是 V 的背包。每件物品只能使用一次。

第 i 件物品的体积是 vi，价值是 wi。

求解将哪些物品装入背包，可使这些物品的总体积不超过背包容量，且总价值最大。
输出最大价值。

"""
# N, V = list(map(int, input().split())) # 物品件数和总体积
# v = [0] * (N + 1) # 保存每件物品的体积
# w = [0] * (N + 1) # 保存每件物品的价值
# for i in range(1, N+1):
#     v_, w_= list(map(int, input().split()))
#     v[i] = v_
#     w[i] = w_
# # 二维DP ,f(i,j) = 只从前i件物品中选，体积小于等于j的所有选法中价值的最大值
# f = [[0]*(V+1) for i in range(N+1)]
# for i in range(1, N+1):
#     for j in range(V+1):
#         if v[i] > j: # 不能将第i件物品装进去
#             f[i][j] = f[i-1][j]
#         else:
#             f[i][j] = max(f[i-1][j], f[i-1][j-v[i]] + w[i])
#
# print(f[N][V])

"""
    可以对上述的二维DP进行优化，在求f[i][j]时只用到了i-1层的信息
"""
N, V = list(map(int, input().split())) # 物品件数和总体积
v = [0] * (N + 1) # 保存每件物品的体积
w = [0] * (N + 1) # 保存每件物品的价值
for i in range(1, N+1):
    v_, w_= list(map(int, input().split()))
    v[i] = v_
    w[i] = w_

# 一维DP
f = [0]*(V+1)
for i in range(1, N+1):
    for j in range(V, v[i]-1, -1): # 从后往前
        f[j] = max(f[j], f[j-v[i]] + w[i])
print(f[V])
