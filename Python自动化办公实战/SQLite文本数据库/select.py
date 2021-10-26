# -*- coding:utf8 -*-
# @Time：2021/10/26 10:34 上午
# @Author： Huang Jeff

import sqlite3
import pathlib
# 数据库文件的路径和文件名称
dir = pathlib.PurePath(__file__).parent
db = pathlib.PurePath(dir, "contents.db")

# 创建连接
conn = sqlite3.connect(db)

# 创建游标
cur = conn.cursor()

# 定义要执行的sql语句
sql2 = '''SELECT phone FROM address_book WHERE name = "Tom" '''

# 执行SQL
try:
    result = cur.execute(sql2)
    print(result.fetchone())

except Exception as e:
    print(f"失败的原因:{e}")

finally:
    cur.close()
    conn.close()
