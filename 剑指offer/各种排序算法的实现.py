# -*- coding: utf-8 -*-

"""
__author__ = "BigBrother"

"""


class MaoPao:
    @staticmethod
    def sort(array):
        end = len(array) - 1
        for i in range(end, 0, -1):
            flag = False
            for j in range(0, i):
                if array[j] > array[j+1]:
                    flag = True
                    array[j], array[j+1] = array[j+1], array[j]
            if flag == False:
                break
        return array



class SelectSort:
    @staticmethod
    def sort(array):
        end = len(array) - 1
        for i in range(0, end):
            min_idx = i
            for j in range(i+1, end + 1):
                if array[j] < array[min_idx]:
                    min_idx = j
            array[i], array[min_idx] = array[min_idx], array[i]

        return array

class InsertSort:
    @staticmethod
    def sort(array):
        end = len(array) - 1
        for i in range(1, end+1):
            for j in range(i, 0, -1): # 找插入位置
                if array[j] < array[j-1]:
                    array[j], array[j-1] = array[j-1], array[j]
        return array


class ShellSort:

    def sort(self, array):
        d = len(array) // 2 # 增量
        while d > 0:
            for i in range(0, d):
                self.insert_sort_gap(array, i, d)
            print("增量为：{},排序后的列表为：{}".format(d, array))
            d = d // 2
        return array

    def insert_sort_gap(self, array, start_idx, gap):
        """将每一个子列表进行插入排序"""

        end = len(array) - 1   # 获取每个列表的结束位置

        for i in range(start_idx + gap, end + 1, gap):
            current_value = array[i]
            position = i
            while position >= gap and current_value < array[position-gap]:
                array[position], array[position - gap] = array[position - gap], array[position]
                position -= gap
            array[position] = current_value




class MergeSort:
    def merge_sort(self, array, start, end):
        if start >= end:
            return
        mid = (start + end) // 2
        self.merge_sort(array, start, mid)
        self.merge_sort(array, mid+1, end)
        self.merge(array, start, end)
        return array

    def merge(self, array, start,  end):
        mid = (start + end) // 2
        left = array[start:mid+1] # ！！！！
        right = array[mid+1:end+1]

        i = j = 0
        k = start # ！！！
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1


class QuickSort:
    # def __init__(self, array):
    #     self.array = array

    def quick_sort(self, array, start, end):
        if start >= end: # 只有一个元素
            return
        p = self.partition(array, start, end) # 基元的位置
        # print(p)
        self.quick_sort(array, start, p-1)
        self.quick_sort(array, p+1, end)

        return array

    def partition(self, array, start, end):
        """找到基元的正确位置"""
        pivot = array[start]

        p1 = start + 1
        p2 = end
        while p1 <= p2:
            while p1 <= p2 and array[p1] <= pivot:
                p1 += 1
            while p1 <= p2 and array[p2] >= pivot:
                p2 -= 1
            if p1 < p2:
                array[p1], array[p2] = array[p2], array[p1]

        array[start] , array[p2] = array[p2], array[start] # 将基元放在正确位置上

        return p2


class HeapSort:
    def heap_sort(self):
        pass



if __name__ == "__main__":
    array = [10,9,8,7,6,5,4,3,2,1]
    # maopao = MaoPao()
    # print("maopao:", maopao.sort(array))
    # xuanze = SelectSort()
    # print("xuanze:", xuanze.sort(array))
    # insert = InsertSort()
    # print("insert:", insert.sort(array))
    # shell_sort = ShellSort()
    # print("shell:", shell_sort.sort(array))
    # merge_sort = MergeSort()
    # print(merge_sort.merge_sort(array, 0, len(array)-1))
    quick = QuickSort()
    print(quick.quick_sort(array, 0, len(array)-1))