# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 17:07:28 2022

@author: MuhammadAkbar
"""

# import math
import random as r

# uzunlik = lambda PI, r : 2*PI*r
# print(uzunlik(math.pi, 10))


# def daraja(n):
#     return lambda x : x**n

# kvadrat = daraja(2)
# print("5 ning kvadrati = ", kvadrat(5))
# print("9 ning kvadrati = ", kvadrat(9))

# kub = daraja(3)
# print("5 ning kubi = ", kub(5))
# print("9 ning kubi = ", kub(9))


# sonlar = list(range(11))
# ildizlar = list(map(math.sqrt, sonlar))
# kvadratlar = list(map(lambda x : x*x, sonlar))


sonlar = r.sample(range(100), 10)
print(sonlar)

def juftmi(x):
    return x % 2 == 0

# juft_sonlar = list(filter(juftmi, sonlar))
# print(juft_sonlar)
juft_sonlar = list(filter(lambda x : x%2==0, sonlar))
print(juft_sonlar)