# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 14:25:39 2024

@author: Huỳnh Văn Thiên 23730711
"""

print('Nhâp vào giờ, phút, giây')
a = float(input('Giờ = '))
b = float(input('Phút = '))
c = float(input('Giây = '))
if  a == 0 and b == 0 and c == 0:
    print('Không hợp lệ')  
else:    
    print('Số giây được đổi là', a * 3600 + b * 60 + c  )
