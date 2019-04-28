# -*- coding: utf-8 -*-

"""
__author__ == "BigBrother"

"""


class Solution:
    def test(self, target):
        """和为target的连续正数序列"""
        if target < 3:
            return []

        """
            用prefix[i]表示以下标i结尾的前缀和
        """
        count = 0
        prefix = []
        prefix.append(0) # 第一项为0
        for num in range(1,target+1): # 前缀和数组
            count += num
            prefix.append(count)
        p1 = 0
        p2 = 0

        res = []
        while p1 <= p2 and p2 < len(prefix):
            while p1 <= p2 and p2 < len(prefix) and prefix[p2] - prefix[p1] < target:
                p2 += 1
            while p1 <= p2 and p2 < len(prefix) and prefix[p2] - prefix[p1] == target:
                if p2 - p1 >=2: # 序列长度为2才保存
                    res.append([i for i in range(p1+1, p2+1)])
                p2 += 1
                p1 += 1
            while p1 <= p2 and p2 < len(prefix) and prefix[p2] - prefix[p1] > target:
                p1 += 1
        return res

if __name__ == "__main__":
    s = Solution()
    print(s.test(3))