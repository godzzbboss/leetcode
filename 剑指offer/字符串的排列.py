# -*- coding: utf-8 -*-

"""
__author__ == "BigBrother"

"""

import copy
class Solution:
    def test(self, s):
        result = set() # 传入递归函数，用来保存结果
        s = list(s) # 将字符串变为字符列表
        self.permutate(s, 0, result)
        result = sorted(result) # 按字典序排序
        return result


    def permutate(self, s, start, result):
        if not s:
            return None
        if start == len(s) - 1: # 遍历到字符串最后一个字符
            if "".join(s) not in result:
                result.add("".join(s)) # 加入集合，用来防止元素重复
            return None
        else:
            for i in range(start, len(s)):
                s[start], s[i] = s[i], s[start]
                self.permutate(s, start+1, result)
                s[start], s[i] = s[i], s[start]


if __name__ == "__main__":
    s = Solution()
    ss = "abb"
    print(s.test(ss))