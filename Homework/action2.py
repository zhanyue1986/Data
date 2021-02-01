# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 10:15:24 2021

@author: Jiayiying
"""

#班里有5名同学，现在需要你用Python来统计下这些人在语文、英语、数学中的平均成绩、最小成绩、最大成绩、方差、标准差。
#然后把这些人的总成绩排序，得出名次进行成绩输出

'''import numpy as np
persontype = np.dtype({'names':['name', 'chinese', 'math', 'english'], \
							'formats':['S32', 'i', 'i', 'i']})
peoples = np.array([("ZhangFei",68,65,30),("GuanYu",95,76,98), \
						("LiuBei",98,86,88),("DianWei",90,88,77),\
                            ("XuChu",80,90,90)], dtype=persontype)
print(peoples)
'''
from pandas import DataFrame
data = {'Chinese': [68, 95, 98, 90,80], 'Math': [65, 76, 86, 88, 90], 'English': [30, 98, 88, 77, 90]}
df = DataFrame(data, index=['ZhangFei', 'GuanYu', 'LiuBei', 'DianWei', 'XuChu'], columns=['Chinese', 'Math', 'English'])
print(df)
a=df.mean()#求每一列平均值
print(a)
b=df.min()#求每一列最小值
print(b)
c=df.max()#求每一列最大值
print(c)
var=df.var()#方差
print(var)
e=df.std()#标准差
print(e)
df1=df['score_sum'] = df.sum(axis=1)
print(df1)#每个人的总成绩
df2=df.sort_values('score_sum', ascending=False)
print(df2)#总成绩排名

