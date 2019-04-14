# -*- coding: utf-8 -*-

"""
__author__ == "BigBrother"

"""


class Solution:
    # def test(self, n, m):
    #     """这是一个约瑟夫环问题"""
    #     if n <= 0 or m <= 0:
    #         return -1
    #     count = n
    #     array = [i for i in range(n)]
    #     step = 0 # 记录走了多少步，每走m步清零
    #     idx = -1 # 记录上一次删除数的位置
    #     while count > 0:
    #         idx += 1 # 从上一次删除数的下一位开始
    #         if idx >= n: idx = 0 # 模拟环
    #         if array[idx] == -1: continue # 如果已经删除，则跳过
    #         step += 1
    #         if step == m: # 走了m步, 删除相应元素
    #             array[idx] = -1
    #             step = 0
    #             count -= 1
    #     return idx

    def test(self, n):
        """如果m是不定长的"""
        if n <= 0:
            return -1
        array = [i for i in range(n)]
        count = n
        idx = 0
        step = 0
        m = 1
        while count > 0:
            idx += 1
            if idx >= n: idx = 0
            if array[idx] == -1: continue
            step += 1
            if step == m:
                array[idx] = -1
                step = -1 # 注意这个地方
                m += 1
                count -= 1
        return idx



if __name__ == "__main__":
    s = Solution()
    print(s.test(10))