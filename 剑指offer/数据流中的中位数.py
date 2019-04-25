# -*- coding: utf-8 -*-

"""
__author__ == "BigBrother"

"""

import heapq
class Solution:
    max_heap = [] # 保存排序后数组的左半部分
    min_heap = [] # 保存排序后数组的右半部分
    def insert(self, num):
        """获取数据流"""
        if len(self.max_heap) + len(self.min_heap) & 1 == 0: # 数组的总长度为偶数
            # 往左半部分插入，即插入最大堆
            if len(self.min_heap) and self.min_heap[0] < num:
                # 先插入最小堆，然后得到最小堆的最小元素插入最大堆
                num = heapq.heappushpop(self.min_heap, num)
            heapq.heappush(self.max_heap, -num)
        else: # 数组的总长度为奇数，插入最小堆
            if len(self.max_heap) and num < -self.max_heap[0]:
                # 先插入最大堆，然后得到最大堆的最大元素插入最小堆
                num = -heapq.heappushpop(self.max_heap, -num)
            heapq.heappush(self.min_heap, num)

    def getMedian(self):
        """获取数据流中的中位数"""
        if len(self.min_heap) + len(self.max_heap) == 0:
            return None
        if len(self.min_heap) + len(self.max_heap) & 1 == 1: # 总的数组长度为奇数
            return -self.max_heap[0]
        if len(self.min_heap) + len(self.max_heap) & 1 == 0: # 总的数组长度为偶数
            return (self.min_heap[0] - self.max_heap[0]) / 2



if __name__ == "__main__":
    pass