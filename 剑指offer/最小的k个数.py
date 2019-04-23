# -*- coding: utf-8 -*-

"""
__author__ == "BigBrother"

"""

import heapq
class Solution:
    def test(self, array, k):
        """使用最大堆实现"""
        if not array or len(array) < k or k == 0:
            return []

        heap = [] # 建立一个空堆
        for i in range(k):
            heapq.heappush(heap, -array[i])

        for j in range(k, len(array)):
            if array[j] < -heap[0]:
                heapq.heapreplace(heap, -array[j])

        return [-i for i in reversed(sorted(heap))]



if __name__ == "__main__":
    pass