# -*- coding: utf-8 -*-

"""
__author__ = "BigBrother"

"""


class Solution(object):
    def get_duplicate_num(self, array):
        """时间复杂度O(n)"""
        if len(array) == 0:
            return -1
        for i in array:
            if i < 0 or i > len(array) - 1:
                return -1

        d = {}
        duplicate_num = []
        for i in array:
            if d.__contains__(i):
                d[i] += 1
                if i not in duplicate_num:
                    duplicate_num.append(i)
            else:
                d[i] = 0
                d[i] += 1
        return duplicate_num


if __name__ == "__main__":
    s = Solution()
    array = [1,2,3,3,4,2]
    print(s.get_duplicate_num(array))

