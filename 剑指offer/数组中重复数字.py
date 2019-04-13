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
    #     for i in range(len(array)): # 检查是否存在不合法数据
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

    # 空间复杂度为O（1），但不改变数组, 使用二分查找在数据范围内查找数据
    def duplicate(self, array, duplication):
        if not array:
             return False
        for num in array:
            if num < 1 or num > len(array) - 1:
                return False
        num_range = [i for i in range(1, len(array))]
        low = 0
        high = len(num_range) - 1
        while low < high:
            mid = (low + high) // 2
            left_array = num_range[:mid+1]
            left_count = self.get_count(left_array, array)
            if left_count > len(left_array):
                high = mid
            else:
                low = mid + 1
        duplication[0] = num_range[low]
        return duplication


    def get_count(self, array1, array2):
        """统计array1中元素在array2中出现的次数"""
        count = 0
        for i in array1:
            for j in array2:
                if i == j:
                    count += 1
        return count







if __name__ == "__main__":
    s = Solution()
    array = [1,3,4,3,2]
    # print(s.get_duplicate_num(array))
    duplication = [-1]
    print(s.duplicate(array, duplication))
