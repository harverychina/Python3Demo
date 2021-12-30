# -*- coding:utf8 -*-
# @Time：2021/12/29 10:34 AM
# @Author： Huang Jeff


result = [(x, y) for x in range(10) for y in range(5) if x * y > 10]

print(result)

result = []
for x in range(10):
    for y in range(5):
        if x * y > 10:
            result.append((x, y))


print(result)


# 不要使用is在整数区间当中比较，因为is是比较内存地址空间非值相等比较

# 错误
x = 27
y = 27
print(x is y)

x = 721
y = 721
print(x is y)

# 正确
x = 27
y = 27
print(x == y)

x = 721
y = 721
print(x == y)


class MyObject(object):
    def __eq__(self, other):
        if other:
            return self.field == other.field
        return True


x = MyObject()

# 错误
# print(x == None)

# 正确，当和None比较时候永远使用is
print(x is None)


# 错误
def pay(name, salary=None):
    # 当明确想要比较对象是否None时，一定要显式地用is None
    # if not salary:          # 错误
    if salary is not None:    # 正确
        salary = 11
    print(name, "is compensated", salary, "dollars")


# 错误
adict = {i: i * 2 for i in range(10000000)}

# keys()方法会在遍历前生成一个临时的列表，导致上面的代码消耗大量内存并且运行缓慢
# for key in adict.keys():
for key in adict:
    print("{0}".format(key))
