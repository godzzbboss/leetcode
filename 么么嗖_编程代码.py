# -*- coding: utf-8 -*-

class Solution1:
    def answer(self, array):
        """positive num to left, negative num to right"""
        if not array:
            return []
        p1 = 0
        p2 = len(array) - 1

        while p1 < p2:
            # suppose zero is positive
            while p1 < p2 and array[p1] >= 0:
                p1 += 1
            while p1 < p2 and array[p2] < 0:
                p2 -= 1
            array[p1], array[p2] = array[p2], array[p1]
            p1 += 1
            p2 -= 1
        return array


class Solution2:
    def answer(self, dict):
        if not dict:
            return {}
        res = {}
        for k, val in dict.items():
            k_ = k.split(".")
            new_item = self.helper1(k_, val, 0)
            new_item_key = list(new_item.keys())[0]
            # print(res)
            if new_item_key in res:
                res[new_item_key] = self.helper2(res[new_item_key], new_item[new_item_key])
            else:
                res.update(self.helper1(k_, val, 0))

        return res

    def helper1(self, keys, val, idx):
        """keys is a list of char"""
        res = {}
        if len(keys) == 1:
            res[keys[0]] = val
        else:
            res[keys[0]] = self.helper1(keys[idx + 1:], val, idx)

        return res

    def helper2(self, dict1, dict2):
        """dict1 or dict2 is a dictionary that only has one elem"""
        res = {}
        k1, k2 = list(dict1.keys())[0], list(dict2.keys())[0]
        val1, val2 = dict1[k1], dict2[k2]
        if k1 != k2:
            res[k1] = val1
            res[k2] = val2
            return res
        else:
            res[k1] = self.helper2(val1, val2)

        return res


if __name__ == "__main__":
    s1 = Solution1()
    s2 = Solution2()
    print("solution of first problem: ", end="")
    array = [6, 4, -3, 5, -2, -1, 0, 1, -9]
    print(s1.answer(array))

    print("solution of second problem: ", end="")
    d1 = {"A": 1, "B.A": 2, "B.B": 3, "CC.D.E": 4, "CC.D.F": 5}
    print(s2.answer(d1))