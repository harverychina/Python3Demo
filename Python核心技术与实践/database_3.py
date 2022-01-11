# -*- coding:utf8 -*-
# @Time：2022/1/11 12:08 PM
# @Author： Huang Jeff


import MySQLdb
import numpy as np


def test_pymysql():
    conn = MySQLdb.connect(
        host='localhost',
        port=3306,
        user='your_username',
        passwd='your_password',
        db='mysql'
    )

    cur = conn.cursor()
    cur.execute('''
            SELECT
              BTCUSD
            FROM
              price
            WHERE
              timestamp > now() - interval 60 minute
    ''')

    BTCUSD = np.array(cur.fetchall())
    print(BTCUSD.max(), BTCUSD.min())

    conn.close()


if __name__ == "__main__":
    test_pymysql
