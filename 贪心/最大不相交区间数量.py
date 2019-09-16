# -*- coding: utf-8 -*-

"""
__author__ == "BigBrother"

"""
"""
给定N个闭区间[ai,bi]，请你在数轴上选择若干区间，使得选中的区间之间互不相交（包括端点）。

输出可选取区间的最大数量。

输入格式
第一行包含整数N，表示区间数。

接下来N行，每行包含两个整数ai,bi，表示一个区间的两个端点。

输出格式
输出一个整数，表示可选取区间的最大数量。

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
    points.append([l, r])
points.sort(key=lambda item: item[1]) # 按区间右端点进行排序
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