# -*- coding:utf8 -*-
# @Time：2021/11/2 9:16 上午
# @Author： Huang Jeff

import yagmail

conn = yagmail.SMTP(
    user="harvery2004@126.com",
    password="Harverychina2004",
    host="smtp.126.com",
    port=465
)

content = "hello world"
body = f"模板{content}"

conn.send("harverychina@126.com", "主题", body)
