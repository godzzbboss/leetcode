# -*- coding: utf-8 -*-

"""
__author__ = "BigBrother"

"""


class KMP:
    def __init__(self):
        pass

    def get_max_prefix_suffix(self, s):
        pass

    def get_next(self, t):
        """
            next[i]: t[0:i]这个子串的最长真前后缀的长度
        :param t:
        :return:
        """
        len_t = len(t)
        next = [0 for i in range(len_t)]
        i = 0 # t的下标
        j = -1 # i始终要比j大，j的值等于[0,i-1]这个区间字符串的最长真前后缀长度
        next[0] = -1 # 规定
        while(i < len_t-1):
            if j == -1 or t[i] == t[j]:
                i+=1
                j+=1
                next[i] = j
            else:
                j = next[j]
        return next

    def get_nextval(self, t):
        pass

    def get_index(self, s, t):
        """
            返回t在s中首次出现的位置
        :param s:
        :param t:
        :return:
        """
        len_s = len(s)
        len_t = len(t)
        i = j = 0 # 两个指针，分别指向s,t
        next = self.get_next(t)
        while i < len_s and j < len_t:
            if j == -1 or s[i] == t[j]: # j=-1 说明模式串t的第一个字符就与主串第i个位置不同，所以i与j都要加1
                i+=1
                j+=1
            else:
                j = next[j] # 回溯
        if j >= len_t:
            return i-j
        return -1





kmp = KMP()
s = "cdababc"
t = "ababc"
print(kmp.get_next(t))
print(kmp.get_index(s, t))