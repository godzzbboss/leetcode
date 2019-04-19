# -*- coding: utf-8 -*-

"""
__author__ = "BigBrother"

"""

import heapq

def get_top_k(array, k):
    """返回array中第k大元素, 总的时间复杂度为O(nlogk)"""
    if not array or len(array)<k:
        return None

    heap = [] # 空堆
    for i in range(0, k): # 时间复杂度为O(k)
        heapq.heappush(heap, array[i]) # 数组的前k个元素入堆
    for j in range(k, len(array)): # 时间复杂度为O(nlogk)
        if array[j] > heap[0]:
            heapq.heapreplace(heap, array[j])

    return heap[0]

def get_top_ks(array, k):
    """返回前k大元素"""
    if not array or len(array) < k:
        return None
    heap = []
    for i in range(0, k):
        heapq.heappush(heap, array[i])
    for j in range(k, len(array)):
        if array[j] > heap[0]: # 比堆顶元素大
            heapq.heapreplace(heap, array[j])

    return sorted(heap, reverse=True)

def get_bottom_k(array, k):
    """返回第k小的元素"""
    if not array or len(array) < k:
        return None
    heap = []
    for i in range(0, k):
        heapq.heappush(heap, -array[i]) # 创建大顶堆
    for j in range(k, len(array)):
        if -array[j] > heap[0]: # 比堆顶元素小
            heapq.heapreplace(heap, -array[j])

    return - heap[0]



array = [1,2,3,4,1,6,23,14]
# print(get_top_ks(array, 6))
print(get_bottom_k(array, 3))

