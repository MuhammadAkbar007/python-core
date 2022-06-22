# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 20:27:04 2022

@author: user
"""

import random

def son_top(x=10):
    son = random.randint(1, x)
    print(f"Men 1 va {x} orasida bir son o'yladim. Topa olasizmi ?")
    tahminlar = 0
    while True:
        tahminlar += 1
        tahmin = int(input("Tahmin qilgan soningizni kiriting >>> "))
        if tahmin > son: print("Xato! Men o'ylagan son bundan kichikroq. Yana harakat qiling")
        elif tahmin < son : print("Xato! Men o'ylagan son bundan kattaroq. Yana harakat qiling")
        else: break
    print(f"To'g'ri ! Siz {tahminlar} ta urinishda topdingiz")
    return tahminlar
    
def son_top_pc(x=10):
    input(f"1 va {x} orasida bir son o'ylang va istalgan tugmani bosing. Men topaman >>> ")
    tahminlar = 0
    quyi = 1
    yuqori = x
    while True:
        tahminlar += 1
        if quyi != yuqori: son = random.randint(quyi, yuqori)
        else: son = quyi
        javob = input(f"Siz {son} sonini o'yladingiz: to'g'ri (t),"
                      f"men o'ylagan son bundan kattaroq (+) yoki kichikroq (-) >>> ".lower())
        if javob == '-': yuqori = son - 1
        elif javob == '+': quyi = son + 1
        else: break
    print(f"{tahminlar} ta urinishda topdim !")
    return tahminlar

def play(x=10):
    javob = 1
    while javob:
        tahminlar_user = son_top(x)
        tahminlar_pc = son_top_pc(x)
        if tahminlar_user > tahminlar_pc: print("Men yutdim !")
        elif tahminlar_user < tahminlar_pc: print("Siz yutdingiz !")
        else: print("Durrang !")
        javob = int(input("Yana o'ynaysizmi ? Ha(1) / Yo'q(0) >>> "))