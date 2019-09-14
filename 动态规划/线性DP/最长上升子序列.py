# -*- coding: utf-8 -*-

"""
__author__ == "BigBrother"

"""
"""
给定一个长度为N的数列，求数值严格单调递增的子序列的长度最长是多少。

输入格式
第一行包含整数N。

第二行包含N个整数，表示完整序列。

输出格式
输出一个整数，表示最大长度。

数据范围
1≤N≤1000，
−109≤数列中的数≤109
输入样例：
7
3 1 2 1 8 5 6
输出样例：
4

"""

n = int(input())
array = list(map(int, input().split()))
array.insert(0, 0)
N = 1010
f = [0] * N
for i in range(1, n + 1):
    f[i] = 1 # 以第i个数结尾的最长上升子序列的长度最小为1
    for j in range(1, i):
        if array[i] > array[j]:
            f[i] = max(f[i], f[j] + 1)
res = 0
for i in range(1, n+1):
    res = max(res, f[i])
print(res)

