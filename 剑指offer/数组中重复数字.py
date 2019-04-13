# -*- coding: utf-8 -*-

"""
__author__ = "BigBrother"

"""


class Solution(object):
    def get_duplicate_num(self, array):
        """时间复杂度O(n)"""
        if len(array) == 0:
            return -1
        d = {}
        duplicate_num = []
        for i in array:
            if i < 0 or i > len(array) - 1:
                return -1
            if d.__contains__(i):
                if i not in duplicate_num:
                    duplicate_num.append(i)
            else:
                d[i] = 1

        return duplicate_num

    # 空间复杂度为O（1）
    # def duplicate(self, array, duplication):
    #     # write code here
    #     if not array:
    #         return False
    #     for i in range(len(array)):
    #         if array[i] < 0 or array[i] > len(array) - 1:
    #             return False
    #     for i in range(len(array)):
    #         # print(i)
    #         while i != array[i]:
    #             if array[i] == array[array[i]]:
    #                 duplication[0] = array[i]
    #                 return True
    #             temp = array[i]
    #             array[i], array[temp] = array[temp], array[i]
    #     return False



if __name__ == "__main__":
    s = Solution()
    array = [1,2,3,0]
    # print(s.get_duplicate_num(array))
    duplication = [-1]
    print(s.duplicate(array, duplication))
