# -*- coding: utf-8 -*-

"""
__author__ == "BigBrother"

"""
"""
给定两个字符串A和B，现在要将A经过若干操作变为B，可进行的操作有：

删除–将字符串A中的某个字符删除。
插入–在字符串A的某个位置插入某个字符。
替换–将字符串A中的某个字符替换为另一个字符。
现在请你求出，将A变为B至少需要进行多少次操作。

输入格式
第一行包含整数n，表示字符串A的长度。

第二行包含一个长度为n的字符串A。

第三行包含整数m，表示字符串B的长度。

第四行包含一个长度为m的字符串B。

字符串中均只包含小写字母。

输出格式
输出一个整数，表示最少操作次数。

数据范围
1≤n,m≤1000
输入样例：
10 
AGTCTGACGC
11 
AGTAAGTAGGC
输出样例：
4
"""
n = int(input())
s1 = list(input())
s1.insert(0, 0)
m = int(input())
s2 = list(input())
s2.insert(0, 0)
N = 1010
f = [[0] * N for i in range(N)]

for i in range(n+1): f[i][0] = i
for i in range(m+1): f[0][i] = i

for i in range(1, n + 1):
    for j in range(1, m + 1):
        f[i][j] = min(f[i][j-1] + 1, f[i-1][j] + 1)
        if s1[i] == s2[j]:
            f[i][j] = min(f[i][j], f[i-1][j-1])
        else:
            f[i][j] = min(f[i][j], f[i-1][j-1] + 1)
print(f[n][m])