# -*- coding: utf-8 -*-
"""
Created on Wed May  4 14:25:19 2022

@author: MuhammadAkbar
"""

car_0 = {'model': 'ferrari', 'rang': 'qizil'}
# print(car_0['model'])
# print(car_0['rang'])
car_0['raqam'] = '50 R 510 HA'
# print(car_0)

# del car_0['raqam'] #attrni o'chirib tashlaydi
# print(car_0)

attr = car_0.get('davlati', 'Bunday axborot mavjud emas !')
# print(attr)

# print(car_0.items())
for kalit, qiymat in car_0.items():
    print(f"Key: {kalit}")
    print(f"Value: {qiymat} \n")
    
for kalit in car_0.keys():
    print(kalit)