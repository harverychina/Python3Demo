# -*- coding:utf8 -*-
# @Time：2021/10/21 9:19 上午
# @Author： Huang Jeff

from requests_html import HTMLSession

# url = "https://unsplash.com/photos/NLzaiXOELFY/download"
url = "https://unsplash.com/photos/7RhVpW9JIv4/download?ixid=MnwxMjA3fDB8MXxhbGx8fHx8fHx8fHwxNjM0NzgyMzMy&force=true"

session = HTMLSession()

result = session.get(url)

print(result.status_code)

with open("one.jpg", "wb") as f:
    f.write(result.content)
