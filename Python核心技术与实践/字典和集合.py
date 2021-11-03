# -*- coding:utf8 -*-
# @Time：2021/11/3 9:19 上午
# @Author： Huang Jeff

d1 = {'name': 'jason', 'age': 20, 'gender': 'male'}
d2 = dict({'name': 'jason', 'age': 20, 'gender': 'male'})
d3 = dict([('name', 'jason'), ('age', 20), ('gender', 'male')])
d4 = dict(name='jason', age=20, gender='male')
print(d1 == d2 == d3 == d4)

s1 = {1, 2, 3}
s2 = set([1, 2, 3])
print(s1 == s2)

s = {1, 'hello', 5.0}

d = {'name': 'jason', 'age': 20}
print(d['name'])
# 输出不存存的索引值
# print(d['location'])

print(d.get('name'))
# 设置一个默认值给location索引
print(d.get('location', 'null'))

# 不支持索引操作，集合是一个哈索表
s3 = {1, 2, 3}
# print(s3[1])
# 判断元素是否存在字典或集合内
print(1 in s)
print(10 in s)

d5 = {'name': 'jason', 'age': 20}
print('name' in d5)
print('location' in d)

# 字典和集合是同时支持增加、删除、更新等操作

d6 = {'name': 'jason', 'age': 20}
d6['gender'] = 'male'
d6['dob'] = '1999-02-01'
print(d6)
# 更新dob值
d6['dob'] = '1998-01-01'
print(d6)
d6.pop('dob')  # 删除dob值
print(d6)

s4 = {1, 2, 3}
s4.add(4)  # 增加元素4到集合
"""
集合删除元素是删除最后一个元素，集合本身是无序，无法知道你是删除哪个元素
"""
print(s4)
s4.remove(4)  # 从集合中删除元素4
print(s4)


# 字典和集合进行排序
d7 = {'b': 1, 'a': 2, 'c': 10}
# 根据字典键的升序排序
d7_sorted_by_key = sorted(d7.items(), key=lambda x: x[0])
print(d7_sorted_by_key)
d7_sorted_by_value = sorted(d7.items(), key=lambda x: x[1])
print(d7_sorted_by_value)

s5 = {3, 4, 2, 1}
s5_sorted = sorted(s5)
print(s5_sorted)

# 字典和集合的性能（查找、添加和删除）

# 查找实例：某电商平台提供根据商品ID查找商品价格

# 集合
products = [
    (143121312, 100),
    (432314553, 30),
    (32421912367, 150),
    (937153201, 30)
]

# 字典
products_1 = {
    143121312: 100,
    432314553: 30,
    32421912367: 150,
    937153201: 60
}

def find_product_price(products, product_id):
    for id, price in products:
        if id == product_id:
            return price

    return none

print('商品143121312的价格是：{}'.format((find_product_price(products, 143121312))))

print('商品432314553的价格是：{}'.format(products_1[432314553]))

"""
集合查找时需要进行每个元素进行排序，然后使用二分查找，时间复杂度很长O(n)，
而字典则采用内部哈希表记得每个元素位置的，所以非常便捷高效，时间复杂度为O(1)
"""

# 查找商品当中有多少种价格（集合）
def find_unique_price_using_list(products):
    # 使用列表保存价格
    unique_price_list = []
    for _, price in products:
        if price not in unique_price_list:
            unique_price_list.append(price)
    return len(unique_price_list)


print('本次商品当中有{}种不同价格'.format((find_unique_price_using_list(products))))

# 查找商品当中有多少种价格（字典）
def find_unique_price_using_set(products):
    # 使用集合保存价格
    unique_price_set = set()
    for _, price in products:
        unique_price_set.add(price)
    return len(unique_price_set)

print('本次商品当中有{}种不同价格'.format((find_unique_price_using_set(products))))

