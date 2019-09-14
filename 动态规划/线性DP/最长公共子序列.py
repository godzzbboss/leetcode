# -*- coding: utf-8 -*-

"""
__author__ == "BigBrother"

"""
"""
给定两个长度分别为N和M的字符串A和B，求既是A的子序列又是B的子序列的字符串长度最长是多少。

输入格式
第一行包含两个整数N和M。

第二行包含一个长度为N的字符串，表示字符串A。

第三行包含一个长度为M的字符串，表示字符串B。

字符串均由小写字母构成。

输出格式
输出一个整数，表示最大长度。

数据范围
1≤N≤1000,

输入样例：
4 5
acbd
abedc
输出样例：
3
"""
n, m = list(map(int, input().split()))
s1 = list(input())
s2 = list(input())
s1.insert(0,0)
s2.insert(0,0)

N = 1010
f = [[0] * N for i in range(N)]
# f[i,j]所有在第一个字符串前i个字符中出现，且在第二个字符串前j个字符中出现的公共子序列
for i in range(1, n + 1):
    for j in range(1, m+1):
        f[i][j] = max(f[i-1][j-1], f[i-1][j], f[i][j-1])
        if s1[i] == s2[j]:
            f[i][j] = max(f[i][j], f[i-1][j-1] + 1)

print(f[n][m])