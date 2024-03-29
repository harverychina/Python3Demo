# -*- coding:utf8 -*-
# @Time：2022/1/11 9:25 AM
# @Author： Huang Jeff


import MySQLdb


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
            CREATE TABLE price (
                timestamp TIMESTAMP NOT NULL,
                BTCUSD FLOAT(8,2),
                PRIMARY KEY (timestamp)
            );
        ''')
    cur.execute('''
            INSERT INTO price VALUES(
                "2019-07-14 14:12:17",
                11234.56
            );
        ''')

    conn.commit()
    conn.close()


if __name__ == "__main__":
    test_pymysql
