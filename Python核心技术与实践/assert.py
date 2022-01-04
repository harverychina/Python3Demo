# -*- coding:utf8 -*-
# @Time：2022/1/4 8:56 AM
# @Author： Huang Jeff


"""
assert 在程序中的作用，是对代码做一些internal的self-check。使用assert，就表示你很确定。这个条件一定会发生或者一定不会发生。
注意：assert 并不适用 run-time error  的检查。
"""


def apply_discount(price, discount):
    updated_price = price * (1 - discount)
    assert 0 <= updated_price <= price, "价格必须大于等于0小于原价"
    return updated_price


def calculate_average_price(total_sales, num_sales):
    assert num_sales > 0, "销售数量必须于0"
    return total_sales / num_sales


if __name__ == "__main__":
    print(apply_discount(100, 0.2))
    # print(apply_discount(100, 2))
    print(calculate_average_price(100, 2))
    # print(calculate_average_price(100, -2))
