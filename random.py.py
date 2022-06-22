# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 16:15:07 2022

@author: MuhammadAkbar
"""

import random as r

# son = r.random()
# print("son = ", son)

# son1 = r.randint(0, 10)
# print("0, 10 oraliqdan son = ", son1)

# ismlar = ['ali', 'vali', 'doston', 'behzod', 'otabek']
# ism = r.choice(ismlar)
# print(ism)
# print(r.choice(ism))

# x = list(range(0, 51, 5))
# print(x)
# print(r.choice(x))

x = list(range(11))
print(x)
r.shuffle(x)
print(x)
