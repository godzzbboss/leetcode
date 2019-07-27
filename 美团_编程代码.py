# -*- coding: utf-8 -*-


def solution1(array, m):
    """数组后置"""
    if not array or len(array) < m:
        return False
    array = helper1(array, 0, len(array) - 1)
    array = helper1(array, 0, len(array) - m - 1)
    return helper1(array, len(array) - m, len(array) - 1)

def helper1(array, start, end):
    """对数组进行翻转"""
    if start > end:
        return False
    while start < end:
        array[start], array[end] = array[end], array[start]
        start += 1
        end -= 1

    return array



def solution2(array1, array2):
    """中位数查找 """
    len1 = len(array1)
    len2 = len(array2)

    total_len = len1 + len2
    if total_len & 1 == 0: # 长度为偶数
        left = find_kth(array1, 0, array2, 0, (total_len - 1) // 2 + 1)
        return left
    else:
        return find_kth(array1, 0, array2, 0, total_len // 2 + 1)

def find_kth(array1, i, array2, j, k):
    """i,j分别为array1和array2开始查找位置， k是要查找的第k个元素"""
    # 保证array1可查找长度大于array2的查找长度
    if len(array1) - i > len(array2) - j:
        return find_kth(array2, j, array1, i, k)
    # 如果array1的可查找长度为0
    if len(array1) == i:
        return array2[j + k - 1]
    # 如果k==1
    if k == 1:
        return min(array1[i], array2[j])

    si = min(i + k // 2, len(array1))
    sj = j + k // 2

    if array1[si - 1] > array2[sj - 1]: # array2可查找范围的前k // 2个元素肯定不是第k个元素，所以不用查找
        return find_kth(array1, i, array2, sj, k - k // 2)
    else:
        return find_kth(array1, si, array2, j, k - (si - i))




if __name__ == "__main__":
    array = ["a", "b", "c", "d", "e", "f", "g"]
    print(solution1(array,3))

    array1 = [1, 3, 5, 7, 9]
    array2 = [0, 2, 4, 6, 8]
    print(solution2(array1, array2))