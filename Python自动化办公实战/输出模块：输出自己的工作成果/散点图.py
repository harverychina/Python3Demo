# -*- coding:utf8 -*-
# @Time：2021/10/28 2:21 下午
# @Author： Huang Jeff

import seaborn as sns
import matplotlib.pyplot as plt

sns.set(style="darkgrid", color_codes=True)
iris = sns.load_dataset('iris', data_home='seaborn-data', cache=True)
# iris = sns.load_dataset('iris', data_home='seaborn-data', cache=True)


fig = sns.pairplot(
    iris,
    kind='scatter',
    diag_kind='hist',
    hue='species',
    palette='husl',
    markers=[
        'o',
        's',
        'D'],
    height=2)


fig.savefig("scatter.jpg", dpi=400)
plt.show()
