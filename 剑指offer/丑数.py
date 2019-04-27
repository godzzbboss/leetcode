# -*- coding: utf-8 -*-

"""
__author__ == "BigBrother"

"""


class Solution:
    def test(self, n):
        """返回从小到大排序的第n个丑数"""
        if n == 0:
            return 0
        choushu_array = [0] * n # 从小到大保存找到的丑数
        choushu_array[0] = 1 # 第一个丑数
        next_choushu_idx = 1 # next_choushu_idx 指向最后一个下一个丑数的位置
        p2 = 0
        p3 = 0
        p5 = 0
        while next_choushu_idx < n:
            next_choushu = min(choushu_array[p2] * 2, choushu_array[p3] * 3, choushu_array[p5] * 5)
            choushu_array[next_choushu_idx] = next_choushu

            while choushu_array[p2] * 2 <= choushu_array[next_choushu_idx]:
                p2 += 1
            while choushu_array[p3] * 3 <= choushu_array[next_choushu_idx]:
                p3 += 1
            while choushu_array[p5] * 5 <= choushu_array[next_choushu_idx]:
                p5 += 1
            next_choushu_idx += 1

        return choushu_array[next_choushu_idx-1]






if __name__ == "__main__":
    s = Solution()
    print(s.test(7))