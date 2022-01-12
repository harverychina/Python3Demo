# -*- coding:utf8 -*-
# @Time：2022/1/11 2:45 PM
# @Author： Huang Jeff
from django.db import models


class Position(models.Model):
    asset = models.CharField(max_length=10)
    timestamp = models.DataTimeField()
    amount = models.DecimalField(max_digits=10, decimal_places=3)
