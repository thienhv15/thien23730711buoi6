# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 18:34:42 2024

@author: Admin
"""

chuoi = "Đại học Quốc gia, Khu phố 6, P. Linh Trung, Q. Thủ Đức, Tp. HCM"
s = chuoi.split(', ')
s[2] = s[2].replace('P. ','')
s[3] = s[3].replace('Q. ','')
s[4] = s[4].replace('Tp. ','')
for s in s:
    print(s)