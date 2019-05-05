# -*- coding: utf8 -*-

def Add(num1, num2):
    # write code here
    """使用异或操作和与操作完成"""
    while num2:
        temp = (num1 ^ num2) & 0xFFFFFFFF
        num2 = ((num1 & num2) << 1) & 0xFFFFFFFF
        num1 = temp
    if num1 > 0x7FFFFFFF: # 这里的num1的最高位符号位真实的数，如果num1>0x7fffffff,说明num1最高位为1，应该是负数
        return ~(num1 ^ 0xFFFFFFFF) # 将无符号数变为有符号数
    return num1 # 如果 num1为正数，则直接返回

print(Add(-1,-1))