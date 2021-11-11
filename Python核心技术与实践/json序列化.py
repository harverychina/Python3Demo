# -*- coding:utf8 -*-
# @Time：2021/11/10 9:36 上午
# @Author： Huang Jeff

import json

params = {
    'symbol': '123456',
    'type': 'limit',
    'price': 123.4,
    'amount': 23
}
# 接受Python的基本数据类型，序列化为string
params_str = json.dumps(params)

print('after json serialization')
print('type of params_str = {}, params_str = {}'.format(type(params_str), params))
# 接受一个合法字符串，然后将其反序列化为Python的基本数据类型
original_params = json.loads(params_str)


