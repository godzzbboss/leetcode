# -*- coding: utf-8 -*-

"""
__author__ == "BigBrother"

"""

from collections import deque
class Solution:
    def test(self, array, size):
        """
        使用单调队列实现，从大到小排序，需要存放每个元素的索引，因为要判断
        队头元素是否还包含在当前滑动窗口内
        """
        if not array or len(array) < size or size <= 0:
            return []

        result = []
        d = deque()
        for i in range(len(array)):
            while d and array[i] > array[d[-1]]: # 如果array[i] > 队尾元素，则队尾元素出队
                d.pop()
            while d and (i - d[0] + 1) > size: # 如果队列中的最大元素不在当前窗口，则从队头出队
                d.popleft()
            d.append(i) # 索引入队
            if d and i + 1 >= size: # 只用当滑动窗口的大小达到size时才记录最大值
                result.append(array[d[0]])

        return result




if __name__ == "__main__":
    pass