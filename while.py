# -*- coding: utf-8 -*-
"""
Created on Fri May 13 18:25:30 2022

@author: MuhammadAkbar
"""

# son = 1
# while son <= 5:
#     print(son, end=' ')
#     son += 1
# print("While ended !")

# print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
# savol = "Istalgan son kiriting. Chiqish uchun exit deb yozing >>> "
# qiymat = ''
# while qiymat != 'exit':
#     qiymat = input(savol)
#     if qiymat != 'exit':
#         print(float(qiymat)**2)
# print("While tugadi")

# savol = "Istalgan son kiriting >>> "
# qiymat = ''
# ishora = True
# while ishora:
#     qiymat = input(savol)
#     if qiymat == 'exit':
#         ishora = False
#     else:
#         print(float(qiymat)**2)
# print("While tugadi !")

# savol = "Istalgan son kiriting >>> "
# qiymat = ''
# while True:
#     qiymat = input(savol)
#     if qiymat == 'exit':
#         break
#     else:
#         print(float(qiymat)**2)
# print("While tugadi !")

# sonlar = list(range(1, 11))
# for son in sonlar:
#     if son == 5:
#         break
#     else:
#         print(f"{son} ning kvadrati = {son**2}")

# sonlar = list(range(1, 11))
# for son in sonlar:
#     if son == 5:
#         continue
#     else:
#         print(f"{son} ning kvadrati = {son**2}")

# son = 0
# while son <= 10:
#     son += 1
#     if son % 2 != 0:
#         continue
#     else:
#         print(son)

# n = 1
# ismlar = []
# while True:
#     savol = f"{n}-do'stingizning ismini kiriting >>> "
#     ism = input(savol)
#     ismlar.append(ism)
#     n += 1
#     more = input("Yana ism qo'shmoqchimisiz ? Ha / Yo'q >>> ")
#     if more.lower() != "ha":
#         break
# print(ismlar)

# dostlar = {}
# ishora = True
# while ishora:
#     ism = input("Do'stingiz ismini kiriting >>> ")
#     yosh = input(f"{ism.title()}ning yoshini kiriting >>> ")
#     dostlar[ism] = int(yosh)
    
#     javob = input("Yana do'st qo'shasizmi ? Ha / Yo'q >>> ")
#     if javob.lower() == "yo'q":
#         ishora = False

# for ism, yosh in dostlar.items():
#     print(f"{ism.title()} {yosh} yoshda !")

talabalar = ['Avazbek', 'Sherzod', 'Bekzod', 'Javohir']
baholangan_talabalar = {}
while talabalar:
    talaba = talabalar.pop()
    baho = input(f"{talaba}ning bahosini kiriting >>> ")
    baholangan_talabalar[talaba] = int(baho)
# print(baholangan_talabalar)
for talaba, baho in baholangan_talabalar.items():
    print(f"{talaba}ning bahosi = {baho}")  