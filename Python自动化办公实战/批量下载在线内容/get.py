# -*- coding:utf8 -*-
# @Time：2021/10/21 9:11 上午
# @Author： Huang Jeff


from requests_html import HTMLSession


name = "猫"
url = f"https://unsplash.com/s/photos/{name}"

session = HTMLSession()

result = session.get(url)

print(result.status_code)
print(result.html.html)
