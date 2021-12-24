#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from matplotlib import pyplot as plt
from matplotlib.font_manager import FontProperties  # 字体库


font = FontProperties(fname=r"C:\Windows\Fonts\方正粗黑宋简体.ttf")

y_1 = [1, 0, 1, 1, 2, 4, 3, 2, 4, 4, 5, 6, 5, 4, 3, 3, 1, 1, 1, 1]
y_2 = [1, 0, 3, 1, 2, 2, 2, 3, 1, 1, 1, 1, 2, 1, 1, 2, 3, 2, 2, 2]
x_1 = range(11, 31)
x_2 = range(11, 31)

# 设置图像的大小
plt.figure(figsize=(15, 9), dpi=80)  # 图片大小 像素

# 设置图中图例内容和位置
plt.plot(x_1, y_1, label='自己', color='r', linestyle='-.')
plt.plot(x_2, y_2, label='同桌', color='b', linestyle='--')
plt.legend(prop=font, loc='upper left')  # upper/lower left/right

# 设置x轴的刻度
_x_1 = list(x_1)
_xticks_label = ["{}岁".format(i) for i in x_1]
plt.xticks(_x_1, _xticks_label, fontproperties=font)
plt.grid(alpha=0.2)  # 添加网格 调整透明度alpha = 0.2

# 坐标轴上面的描述信息
plt.xlabel('岁数', fontproperties=font)
plt.ylabel('个数', fontproperties=font)  # y轴的标题
plt.title("11-31岁的男女朋友的个数", fontproperties=font)  # 顶部的标题

plt.show()  # 展示图像，如果是pycharm中，没有这句话可能就不能够显示图像

'''
在plot中进行添加
color = 'r'  线条颜色
linestyle = '--'  线条风格  -:实线 --：虚线 -.：点划线 默认是实现
linewidth = 5   线条粗细 单位像素
alpha = 0.5  透明度
'''
