# coding:utf-8
"""
学习python的 一种最短路径算法
"""


class Vertex:
    def __init__(self, val, level):
        self.val = val
        self.level = level


def min_operations(a, b):
    visit = []
    q = []  # 模拟队列 list结构
    n = Vertex(a, 0)
    q.append(n)

    while q:
        t = q.pop(0)
        if (t.val == b):
            return t.level
        visit.append(t.val)

        if (t.val * 2 == b or t.val + 1 == b):
            return t.level + 1

        if (t.val * 2) not in visit and (t.val * 2) < b:
            n.val = t.val * 2
            n.level = t.level + 1
            q.append(n)
        if (t.val + 1) not in visit and (t.val + 1) < b:
            n.val = t.val + 1
            n.level = t.level + 1
            q.append(n)


if __name__ == '__main__':
    x, y = 5, 13
    print(min_operations(x, y) - 1)
