# -*- coding:utf8 -*-
# @Time：2021/10/30 11:01 上午
# @Author： Huang Jeff

from PIL import Image

image = Image.open(
    "/Users/huangjiancong/Desktop/Python3Demo/Python自动化办公实战/快速提取图片色块/sunrise.jpg")

image_p = image.convert(
    "P", palette=Image.ADAPTIVE
)

# image_p.show()
# 以列表形式返回图像国调色板
palette = image_p.getpalette()

# 返回此图像中使用的颜色列表, maxcolors默认256
color_counts = sorted(image_p.getcolors(maxcolors=9999), reverse=True)
# 通过颜色列表查找到真正的颜色
colors = []


for i in range(5):
    palette_index = color_counts[i][1]
    dominant_color = palette[palette_index * 3: palette_index * 3 + 3]
    colors.append(tuple(dominant_color))

# 输出颜色
# print(colors)

for i, val in enumerate(colors):
    image.paste(val, (0 + i * 120, 0, 100 + i * 120, 100))

image.save(
    "./Users/huangjiancong/Desktop/Python3Demo/Python自动化办公实战/快速提取图片色块/sunrise2.jpg")
image.show()
