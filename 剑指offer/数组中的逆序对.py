# -*- coding: utf-8 -*-

"""
__author__ == "BigBrother"

"""

# flag = False
# class Solution:
#     counts = 0
#     def test(self, array):
#         if not array:
#             flag = True
#             return 0
#         start = 0
#         end = len(array) - 1
#         self.merge_sort(array, start, end)
#         return self.counts
#
#
#     def merge_sort(self, array, start, end):
#         if start >= end:
#             return 0
#         mid = (start + end) // 2
#         self.merge_sort(array, start, mid)
#         self.merge_sort(array, mid+1, end)
#         self.merge(array, start, mid, end)
#
#     def merge(self, array, start, mid, end):
#         left_array = array[start: mid+1]
#         right_array = array[mid+1: end+1]
#         k = start
#         p1 = 0
#         p2 = 0
#         while p1 < len(left_array) and p2 < len(right_array):
#             if left_array[p1] <= right_array[p2]:
#                 array[k] = left_array[p1]
#                 p1 += 1
#             else:
#                 array[k] = right_array[p2]
#                 p2 += 1
#                 self.counts += (mid - p1 + 1)
#             k += 1
#         while p1 < len(left_array):
#             array[k] = left_array[p1]
#             p1 += 1
#             k += 1
#         while p2 < len(right_array):
#             array[k] = right_array[p2]
#             p2 += 1
#             k += 1


class Solution:
    flag = False
    counts = 0
    def inverse_pairs(self, array):
        """使用归并排序获得array中的逆序对"""
        sorted_array = self.merge_sort(array)
        return self.counts

    def merge_sort(self, array):
        """返回最终排序后的结果"""
        if not array or len(array) == 1: # array为空，或者只有一个元素，直接返回
            return array
        mid = len(array) // 2
        left_array = self.merge_sort(array[:mid])
        right_array = self.merge_sort(array[mid:])

        return self.merge(left_array, right_array)


    def merge(self, array1, array2):
        """将两个有序数组进行合并"""

        p1, p2 = 0, 0
        res = [] # 保存最终排序的结果
        while p1 < len(array1) and p2 < len(array2):
            if array1[p1] <= array2[p2]:
                res.append(array1[p1])
                p1 += 1
            else:
                self.counts += len(array1) - p1
                res.append(array2[p2])
                p2 += 1

        if p1 < len(array1):
            res.extend(array1[p1:])
        if p2 < len(array2):
            res.extend(array2[p2:])

        return res


if __name__ == "__main__":
    s = Solution()
    array = [1,2,3,4,5,6,0]
    print(s.inverse_pairs(array))