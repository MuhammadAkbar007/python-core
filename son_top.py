# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 18:53:41 2022

@author: MuhammadAkbar
"""

import random

def sontop(x=10):
    tasodifiy_son = random.randint(1, x)
    print(f"Men 1 dan {x} gacha son o'yladim. Topa olasizmi ?")
    tahminlar = 0
    while True:
        tahminlar += 1
        tahmin = int(input(">>> "))
        if tahmin < tasodifiy_son: print("Xato ! Men o'ylagan son bundan kattaroq. Yana harakat qiling")
        elif tahmin > tasodifiy_son: print("Xato ! Men o'ylagan son bundan kichikroq. Yana harakat qiling")
        else: break
    print(f"Tabriklaymiz. {tahminlar} ta tahmin bilan topdingiz !")
    return tahminlar

def sontop_pc(x=10):
    input(f"1 dan {x} gacha biror son o'ylang va istalgan tugmani bosing. Men topaman... ")
    quyi = 1
    yuqori = x
    tahminlar = 0
    while True:
        tahminlar += 1
        if quyi != yuqori:
            tahmin = random.randint(quyi, yuqori)
        else: tahmin = quyi
        javob = input(f"Siz {tahmin} sonini o'yladingiz: to'g'ri (t),"
                      f"men o'ylagan son bundan kattaroq (+) yoki kichikroq (-) ... ".lower())
        if javob == '-': yuqori = tahmin - 1
        elif javob == '+': quyi = tahmin + 1
        else: break
    print(f"{tahminlar} ta urinishda topdim !")
    return tahminlar

def play(x = 10):
    yana = True
    while yana:
        tahminlar_user = sontop(x)
        tahminlar_pc = sontop_pc(x)
        if tahminlar_user > tahminlar_pc: print("Men yutdim !")
        elif tahminlar_pc > tahminlar_user: print("Siz yutdingiz !")
        else: print("Durrang !")
        yana = int(input("Yana o'ynaysizmi ? Ha(1)/Yo'q(0))): "))
