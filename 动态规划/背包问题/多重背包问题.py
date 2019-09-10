# -*- coding: utf-8 -*-

"""
__author__ == "BigBrother"

"""
"""
有 N 种物品和一个容量是 V 的背包。

第 i 种物品最多有 si 件，每件体积是 vi，价值是 wi。

求解将哪些物品装入背包，可使物品体积总和不超过背包容量，且价值总和最大。
输出最大价值。

输出格式
输出一个整数，表示最大价值。

数据范围
0<N,V≤100
0<vi,wi,si≤100
输入样例
4 5
1 2 3
2 4 1
3 4 3
4 5 2
输出样例：
10
"""

# N, V = list(map(int, input().split()))
# s = [0] * 110 # 存放每件物品有多少件
# v = [0] * 110
# w = [0] * 110
# f = [[0] * 110 for i in range(110)]
#
# for i in range(1, N+1):
#     v_, w_, s_ = list(map(int, input().split()))
#     s[i] = s_
#     v[i] = v_
#     w[i] = w_
#
# for i in range(1, N+1):
#     for j in range(V+1):
#         for k in range(s[i]+1): # 第i件物品可以选的件数
#             if k * v[i] <= j:
#                 f[i][j] = max(f[i][j], f[i-1][j - k * v[i]] + k * w[i])
#
# print(f[N][V])

"""
多重背包优化为一维DP
"""
# N, V = list(map(int, input().split()))
# s = [0] * 110 # 存放每件物品有多少件
# v = [0] * 110
# w = [0] * 110
# f = [0] * 110
#
# for i in range(1, N+1):
#     v_, w_, s_ = list(map(int, input().split()))
#     s[i] = s_
#     v[i] = v_
#     w[i] = w_
#
# for i in range(1, N+1):
#     for j in range(V+1, -1, -1): # 从大到小
#         for k in range(s[i]+1): # 第i件物品可以选的件数
#             if k * v[i] <= j:
#                 f[j] = max(f[j], f[j - k * v[i]] + k * w[i])
#
# print(f[V])


"""
0<N≤1000 
0<V≤2000
0<vi,wi,si≤2000
上面两种优化方法在N， V, S很大时，会超时， 因为时间复杂度都是O(N*V*S)
下面这种解法的时间复杂度为O(N*V*logS)
"""
N, V = list(map(int, input().split()))
v = [0] * 22010
w = [0] * 22010
f = [0] * 2010
cnt = 0
for i in range(N):
    v_, w_, s_ = list(map(int, input().split()))
    k = 1
    while k <= s_:
        cnt += 1
        v[cnt] = k * v_
        w[cnt] = k * w_
        s_ -= k
        k *= 2
    if s_ > 0:
        cnt += 1
        v[cnt] = s_ * v_
        w[cnt] = s_ * w_

N = cnt

# 0-1背包
for i in range(1, N+1):
    for j in range(V, v[i]-1, -1):
        f[j] = max(f[j], f[j - v[i]] + w[i])
print(f[V])


