# -*- coding: utf-8 -*-
"""
Created on Fri Jun 24 18:49:14 2022

@author: MuhammadAkbar
"""

import datetime as dt

# hozir = dt.datetime.now()
# print(hozir)

# sana = hozir.date()
# print(sana)

# vaqt = hozir.time()
# print(vaqt)

# soat = hozir.hour
# print(soat)

# minute = hozir.minute
# print(minute)

# second = hozir.second
# print(second)

bugun = dt.date.today()
print(bugun)

ertaga = dt.date(2022, 3, 21)
print(f"Ertangi sana {ertaga}")

bugun = dt.date.today()
ramazon = dt.date(2023, 3, 23)
print(f"Ramazonga {(ramazon - bugun).days} kun qoldi")

hozir = dt.datetime.now()
futbol = dt.datetime(2022, 6, 27, 23, 45, 00)
farq = futbol - hozir
print(f"Futbolgacha {farq.days} kunu {int(farq.seconds/3600)} soat qoldi")