# -*- coding:utf8 -*-
# @Time：2022/1/11 2:47 PM
# @Author： Huang Jeff

from django.shortcuts import render


def runoob(request, asset):
    context = {'hello': 'hello world', 'asset': asset}
    return render(request, 'runoob.html', context)
