# -*- coding:utf8 -*-
# @Time：2021/12/30 10:23 AM
# @Author： Huang Jeff

"""
简单的二分搜索，定一个非递减整数数组，和一个target，要求你找到数组中最小的一个数x，可能满足x**x>target。
"""


def comp(x, target):
    return x * x > target


# 二分搜索函数
# def solver(arr, target):
def binary_search(arr, target):
    l, r = 0, len(arr) - 1
    ret = -1
    while l <= r:
        m = (l + r) // 2
        # comp函数
        # if arr[m] * arr[m] > target:
        if comp(arr[m], target):
            ret = m
            r = m - 1
        else:
            l = m + 1
    return ret
    # if ret == -1:
    #     return -1
    # else:
    #     return arr[ret]


# 输出结果
def solve(arr, target):
    id = binary_search(arr, target)

    if id != -1:
        return arr[id]
    return -1


if __name__ == "__main__":
    print(solve([1, 2, 3, 4, 5, 6], 8))
    print(solve([1, 2, 3, 4, 5, 6], 9))
    print(solve([1, 2, 3, 4, 5, 6], 0))
    print(solve([1, 2, 3, 4, 5, 6], 40))

# 算法比赛以上代码是可以，但是工程角度还需要优化，将不同功能的代码拿了出来，每个函数各司其职，阅读性也能得到一定提高。
