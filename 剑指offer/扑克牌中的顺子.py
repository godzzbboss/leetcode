# -*- coding: utf-8 -*-

"""
__author__ == "BigBrother"

"""


class Solution:
    def test(self, array):
        """判断array中的数字是否是顺子
            思路：先对数组进行排序，统计数组中0的个数，即大小王的个数
                 从第一个不为0的数统计两数之间的间隔，看能否用0的完美填充
                 如果两数相同，则不是顺子
        """
        if not array:
            return False
        sorted_array = sorted(array)
        p1 = 0

        while p1 < len(sorted_array) and sorted_array[p1] == 0:
            p1 += 1
        if p1 == 4: # 如果有4个0,无论最后一个数是什么，都能组成顺子
            return True
        p2 = p1
        gap_count = 0 # 记录间隔数
        while p2 + 1 < len(sorted_array):
            if sorted_array[p2] == sorted_array[p2 + 1]:
                return False
            gap_count += sorted_array[p2 + 1] - sorted_array[p2] - 1
            p2 += 1
        if gap_count == p1:
            return True
        return False



if __name__ == "__main__":
    s = Solution()
    array = [2,1,3,4,5]
    print(s.test(array))