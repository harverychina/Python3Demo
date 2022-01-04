# -*- coding:utf8 -*-
# @Time：2022/1/4 9:41 AM
# @Author： Huang Jeff


# 将要被测试的排序函数
import unittest
from unittest.mock import MagicMock


def sort(arr):
    l = len(arr)
    for i in range(0, l):
        for j in range(i + 1, l):
            if arr[i] >= arr[j]:
                tmp = arr[i]
                arr[i] = arr[j]
                arr[j] = tmp


# 编写子类继承unittest.TestCase
class TestSort(unittest.TestCase):

    # 以 test开头的函数将会被测试
    def test_sort(self):
        arr = [3, 4, 1, 5, 6]
        sort(arr)
        # assert 结果跟我们期待的一样
        self.assertEqual(arr, [1, 3, 4, 5, 6])


# mock
class A(unittest.TestCase):
    def m1(self):
        val = self.m2()
        self.m3(val)

    def m2(self):
        pass

    def m3(self):
        pass

    def test_m1(self):
        a = A()
        a.m2 = MagicMock(return_value="custom_val")
        a.m3 = MagicMock()
        a.m1()
        self.assertTrue(a.m2.called)
        a.m3.assert_called_with("custom_val")


if __name__ == "__main__":
    # unittest.main(argv=['first-arg-is-ignored'], exit=False)
    unittest.main()
    mock = MagicMock()
    mock.side_effect = side_effect
    print(mock(1))
    print(mock(-2))
