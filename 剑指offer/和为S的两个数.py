# -*- coding: utf-8 -*-

"""
__author__ == "BigBrother"

"""

class Solution:
    def test(self, array, target):
        """在递增序列中找两个数使其和为target,如果有多对，输出乘机小的那一对"""
        if not array or len(array) == 1:
            return []
        p1 = 0
        p2 = len(array) - 1
        res = []
        while p1 < p2:
            if array[p1] + array[p2] == target:
                res.append([array[p1], array[p2]])
                p1 += 1
                p2 -= 1
            elif array[p1] + array[p2] > target:
                p2 -= 1
            else:
                p1 += 1

        if not res: # 没找到
            return []
        min_num = 9999999999
        min_idx = 0
        for idx, item in enumerate(res):
            if item[0] * item[1] < min_num:
                min_num = item[0] * item[1]
                min_idx = idx
        return res[min_idx]


if __name__ == "__main__":
    s = Solution()
    array = [1,2,3,4,5]
    print(s.test(array, 5))