# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 13:29:19 2024

@author:  Huỳnh Văn Thiên 23730711
"""
import math
print('Nhập vào 2 số thực a,b')
a = float(input('a='))
b = float(input('b='))
c = (math.sqrt(a) - math.sqrt(b)) / (a ** (1/4) - b ** (1/4))
d = (math.sqrt(a) + (a * b) ** (1/4)) / (a ** (1/4) + b ** (1/4))
x = c - d
print('Kết quả:', x)