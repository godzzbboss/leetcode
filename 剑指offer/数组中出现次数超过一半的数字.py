# -*- coding: utf-8 -*-

"""
__author__ == "BigBrother"

"""


class Solution:
    def test(self, array):
        if not self.check(array):
            return None
        mid = len(array) // 2
        start = 0
        end = len(array) - 1
        index = self.partition(array, start, end)  # 得到基元的下标
        while index != mid:
            if index < mid:
                start = index + 1
                index = self.partition(array, start, end)
            else:
                end = index - 1
                index = self.partition(array, start, end)
        return array[index]



    def partition(self, array, start, end):
        """找到基元的最终位置"""
        pivot = array[start]
        p1 = start + 1
        p2 = end

        while p1 <= p2:
            while p1 <= p2 and array[p2] >= pivot:
                p2 -= 1
            while p1 <= p2 and array[p1] <= pivot:
                p1 += 1
            if p1 < p2:
                array[p1], array[p2] = array[p2], array[p1]
        array[start], array[p2] = array[p2], array[start] # 将基元放在最终的位置
        return p2 # 返回基元的位置

    def check(self, array):
        """检查array是否合法"""
        if not array:
            return False
        flag = False
        for i in array:
            count = 0
            for j in array:
                if j == i:
                    count += 1
            if count > len(array) // 2:
                flag = True
                break
        return flag

if __name__ == "__main__":
    s = Solution()
    array = [111,112]
    print(s.test(array))