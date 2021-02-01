# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 15:59:50 2021

@author: Jiayiying
"""
'''
Action3: 对汽车质量数据进行统计
数据集：car_complain.csv
600条汽车质量投诉
Step1，数据加载
Step2，数据预处理
拆分problem类型 => 多个字段
Step3，数据统计
对数据进行探索：品牌投诉总数，车型投诉总数
哪个品牌的平均车型投诉最多
'''

from pandas import DataFrame
import numpy as np
import pandas as pd

#读取csv文件
data=pd.read_csv('car_complain.csv')
#print(data)

#每个品牌下有多少车型
result1 = data.groupby(['brand','car_model']).agg('count')
result1.rename({'一汽-大众':'一汽大众'},inplace=True)
temp=result1.reset_index()
car_model_sum=temp.groupby('brand').agg('count')
df=car_model_sum.sort_values('car_model', ascending=False)
print(df)

#每个品牌总投诉数量
for i in range(600):
    problems=data['problem'][i]
    num=problems.count(',')
    data['problme_sum'] = num
result2=data.groupby('brand').agg('sum')
result2.rename({'一汽-大众':'一汽大众'},inplace=True)
car_complain_sum=result2.groupby('brand').agg('sum')
print(car_complain_sum)

#df3 = pd.merge(df, car_complain_sum, how='outer')
#print(df3)




