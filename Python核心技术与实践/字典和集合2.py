# -*- coding:utf8 -*-
# @Time：2021/11/3 2:43 下午
# @Author： Huang Jeff

"""
初始化了含有100，000个元素的产品，并分别计算了使用列表和集合来统计产品价格数量的运行时间：
"""

import time

products = [
    (143121312, 100),
    (432314553, 30),
    (32421912367, 150),
    (937153201, 30)
]

# 查找商品当中有多少种价格（集合）
def find_unique_price_using_list(products):
    # 使用列表保存价格
    unique_price_list = []
    for _, price in products:
        if price not in unique_price_list:
            unique_price_list.append(price)
    return len(unique_price_list)

# 查找商品当中有多少种价格（字典）
def find_unique_price_using_set(products):
    # 使用集合保存价格
    unique_price_set = set()
    for _, price in products:
        unique_price_set.add(price)
    return len(unique_price_set)


id = [x for x in range(0, 100000)]
price = [x for x in range(200000, 300000)]
products = list(zip(id, price))

# 计算列表版本的时间
start_using_list = time.perf_counter()
find_unique_price_using_list(products)
end_using_list = time.perf_counter()
print('列表运行时间是：{}'.format(end_using_list - start_using_list))
# 列表运行时间是：49.888531578999995
# 计算集合版本的时间
start_using_set = time.perf_counter()
find_unique_price_using_set(products)
end_using_set = time.perf_counter()
print('集合运行时间是：{}'.format(end_using_set - start_using_set))
# 集合运行时间是：0.009104389999997409
