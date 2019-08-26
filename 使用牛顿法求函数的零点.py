# -*- coding: utf-8 -*-

"""
__author__ == "BigBrother"

"""

"""
    求x^3 - 1 = 0的解
"""
import random
# random.seed(1)

def f_g(x):
    return 3*x**2

def f(x):
    return x**3 - 1


def get_res():
    init_x = random.random() # 从[0，1]之间随机选一个浮点数
    # print(init_x)
    x = init_x
    i = 0
    while i < 10000:
        if abs(x**3 - 1) < 1e-9:
            return x
        x -= f(x) / f_g(x) # 牛顿法更新
        i += 1
    return x

print(get_res())