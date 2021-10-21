# -*- coding:utf8 -*-
# @Time：2021/10/21 10:47 上午
# @Author： Huang Jeff


from selenium import webdriver
import time

browser = webdriver.Chrome()

browser = webdriver.Chrome()

browser.get("http://www.jd.com")

time.sleep(10)

content = browser.page_source
print(content)

browser.quit()
