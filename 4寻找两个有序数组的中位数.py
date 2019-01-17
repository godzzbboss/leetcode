# -*- coding: utf-8 -*-

"""
__author__ = "BigBrother"

"""


class Solution():
    # method 1, O（m+n）
    # 找第mid大的元素， 这个方法也可以扩展到找两个有序列表的第i大元素
    # def test(self, array1, array2):
    #     l1 = len(array1)
    #     l2 = len(array2)
    #     point1 = point2 = 0
    #     mid = (l1 + l2) // 2
    #     # flag =  1 if (l1 + l2) % 2 == 0 else 0 # 若l1+l2为偶数，则flag=1,否则为0
    #     array3 = []
    #     for i in range(l1 + l2):
    #         a = array1[point1] if point1 < l1 else float("inf")
    #         b = array2[point2] if point2 < l2 else float("inf")
    #         if a < b:
    #             array3.append(a)
    #             point1 += 1
    #         else:
    #             array3.append(b)
    #             point2 += 1
    #         if i == mid:
    #             return (array3[mid] + array3[(l1 + l2 - 1) // 2]) / 2

    # method 2, O(log(min(m,n)))
    def test(self, array1, array2):
        len1 = len(array1)
        len2 = len(array2)
        if len1 > len2:  # 保证array1 是最短的数组
            array1, array2 = array2, array1
            len1 = len(array1)
            len2 = len(array2)

        low = 0  # 虚拟数组的起始位置
        high = 2 * len1  # 虚拟数组的结束位置
        l1 = l2 = r1 = r2 = 0
        while (low <= high):
            c1 = (low + high) // 2  # array1虚拟化后的分割位置
            c2 = len1 + len2  - c1  # 虚拟数组元素个数为奇数，所以分割时肯定会把一个数一分为2，c1前面有c1+1个元素
                                    # c1+1+c2+1 = (2len1+1+1 + 2len2+1+1)/2-1+1
            l1 = array1[(c1 - 1) // 2] if c1 != 0 else -float("inf") # 通过虚拟数组的分割位置，找到原始数组中的位置
            r1 = array1[c1 // 2] if c1 != 2 * len1 else float("inf") # 当虚拟数组中分割位置为0或最后一个位置时，在原始
            l2 = array2[(c2 - 1) // 2] if c2 != 0 else -float("inf") # 在原始数组中没有对应位置
            r2 = array2[c2 // 2] if c2 != 2 * len2 else float("inf")
            if l1 > r2:
                high = c1 - 1
            elif l2 > r1:
                low = c1 + 1
            else:
                break
        return (max(l1, l2) + min(r1, r2)) / 2


if __name__ == "__main__":
    s = Solution()
    a = [1, 2, 3]
    b = [3, 4]
    print(s.test(a, b))
