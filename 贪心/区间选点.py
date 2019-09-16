# -*- coding: utf-8 -*-

"""
__author__ == "BigBrother"

"""
"""
给定N个闭区间[ai,bi]，请你在数轴上选择尽量少的点，使得每个区间内至少包含一个选出的点。

输出选择的点的最小数量。

位于区间端点上的点也算作区间内。

输入格式
第一行包含整数N，表示区间数。

接下来N行，每行包含两个整数ai,bi，表示一个区间的两个端点。

输出格式
输出一个整数，表示所需的点的最小数量。

数据范围
1≤N≤105,
−109≤ai≤bi≤109 
输入样例：
3
-1 1
2 4
3 5
输出样例：
2
"""
n = int(input())
points = []
for i in range(n):
    l, r = list(map(int, input().split()))
    points.append([l ,r])

points.sort(key=lambda item: item[1])

res = 1
r = points[0][1]
count = 1
while count < len(points):
    if points[count][0] <= r:
        count += 1
    else:
        res += 1
        r = points[count][1]
        count += 1
print(res)