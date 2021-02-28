# coding:utf-8
x = True
country_counter = {}

def addone(country):
    if country in country_counter:
        country_counter[country] += 1
    else:
        country_counter[country] = 1


addone('China')
addone('Japan')
addone('china')
print(len(country_counter))