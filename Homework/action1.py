# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 16:21:59 2021

@author: Jiayiying
"""
#Action1：求2+4+6+8+...+100的求和，用Python该如何写

# for循环
sum = 0
for number in range(2,102,2):
    sum = sum + number
print(sum)


# while循环
sum = 0
number = 2
while number < 101:
       sum = sum + number
       number = number + 2
print(sum)