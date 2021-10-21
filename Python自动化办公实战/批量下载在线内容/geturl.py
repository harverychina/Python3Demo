# -*- coding:utf8 -*-
# @Time：2021/10/21 10:15 上午
# @Author： Huang Jeff


from requests_html import HTMLSession



name = "猫"
url = f"https://unsplash.com/s/photos/{name}"

session = HTMLSession()

result = session.get(url)

print(result.status_code)
print(result.html.xpath('//figure[@itemprop="image"]//a[@rel="nofollow"]/@href'))


# down_list = result.html.xpath('//figure[@itemprop="image"]//a[@rel="nofollow"]/@href')


# def get_picID_from_url():

# def down_one_pic(url):
#     result = session.get(url)
#     filename = get_picID_from_url(url)
#     with open(filename, "wb") as f:
#     f.write(result.content)



# for one_url in down_list:
#     down_one_pic(one_url)
