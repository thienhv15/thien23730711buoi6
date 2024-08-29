# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 14:25:39 2024

@author: Huỳnh Văn Thiên 23730711
"""

print('Nhâp vào giờ, phút, giây')
a = int(input('Giờ = '))
b = int(input('Phút = '))
c = int(input('Giây = '))
if 0 <=a <= 23 and 0 <= b <= 59  and 0 <= c <= 59:
    print('Số giây được đổi là', a * 3600 + b * 60 + c  )
else:
    print('Không hợp lệ')
