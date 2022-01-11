# -*- coding:utf8 -*-
# @Time：2022/1/11 12:02 PM
# @Author： Huang Jeff

import peewee
from peewee import *

db = MySQLDatabase('mysql', user='admin', password='password')


class Price(peewee.Model):
    timestamp = peewee.DateTimeField(primary_key=True)
    BTCUSD = peewee.FloatField()

    class Meta:
        database = db


def test_peewee():
    Price.create_table()
    price = Price(timestamp='2019-0607 13:17:18', BTCUSD='12345.67')
    price.save()


if __name__ == "__main__":
    test_peewee
