# -*- coding: utf-8 -*-
"""
Created on Sat Jun 18 14:23:47 2022

@author: MuhammadAkbar
"""

# def salom_ber():
#     """Salom beruvchi funksiya"""
#     print("Assalomu alaykum")
    
# salom_ber()

# def ismdan_salom_ber(ism):
#     """Ism qabul qilib salom beruvchi funksiya"""
#     print(f"Assalomu alaykum hurmatli {ism.title()} !")
    
# ismdan_salom_ber("Akbar")
# ismdan_salom_ber("akram")

# def print_fullname(ism, familiya):
#     """Ism va familiyani kiritib, to'liq FISH chiqaruvchi funksiya"""
#     print(f"Foydalanuvchi ismi : {ism.title()},\n"
#           f"Foydalanuvchi familiyasi : {familiya.title()}")
    
# print_fullname("akbar", "ahmadjonov")

# def yosh_hisobla(ism, yil):
#     """Ism va tug'ilgan yildan yoshini chiqarish"""
#     print(f"{ism.title()} hozirda {2022-yil} yoshda !")
    
# # yosh_hisobla("akbar", 2000)
# yosh_hisobla(yil = 2000, ism = 'akbar')

# def yosh_hisobla(tugilgan_yil, joriy_yil = 2022):
#     print(f"Hozirgi yoshingiz = {joriy_yil - tugilgan_yil}")
    
# yosh_hisobla(2000, 2020)
# yosh_hisobla(2000)

# def isPrime(son):
#     if son % 2 == 0 : print(f"{son} soni juft !")
#     else : print(f"{son} soni toq !")
        
# isPrime(19)
# isPrime(18)

# def find_bigger(son1, son2):
#     if son1 > son2 : print(f"{son1} soni {son2}dan katta !")
#     elif son2 > son1 : print(f"{son2} soni {son1}dan katta !")
#     else: print(f"{son1} va {son2} sonlari o'zaro teng !")
    
# find_bigger(27, 89)
# find_bigger(76, 23)
# find_bigger(23, 23)

# def darajaga_kotar(x, y = 2):
#     print(f"{x} ning {y}-darajasi = {x**y}")
    
# darajaga_kotar(2, 3)
# darajaga_kotar(8)

# def bolinadimi(son):
#     for n in range(2, 11):
#         if not son % n :
#             print(f"{son} soni {n} ga qoldiqsiz bo'linadi")
            
# bolinadimi(20)

# def oraliq(max, min = 0, qadam = 1):
#     sonlar = []
#     while min < max:
#         sonlar.append(min)
#         min += qadam
#     return sonlar

# print(oraliq(10))
# print(oraliq(10, 3))
# print(oraliq(10, 3, 2))

# def avto_info(kompaniya, model, rang, korobka, yil, narh = None):
#     return {'kompaniya': kompaniya,
#             'model': model,
#             'rang': rang,
#             'korobka': korobka,
#             'yil': yil,
#             'narh': narh}

# avtolar = []
# while True:
#     print("\nQuyidagi ma'lumotlarni kiriting")
#     kompaniya = input("Ishlab chiqaruvchi: ")
#     model = input("Modeli: ")
#     rang = input("Rangi: ")
#     korobka = input("Korobkasi: ")
#     yil = input("Ishlab chiqarilgan yili: ")
#     narh = input("Narhi: ")
    
#     avtolar.append(avto_info(kompaniya, model, rang, korobka, yil))
    
#     javob = input("\nYana avto qo'shasizmi? (yes/no): ")
#     if javob == 'no': break

# print("\nSalonimizdagi avtolar:\n")
# for avto in avtolar:
#     if avto['narh']: narh = avto['narh']
#     else: narh = "Noma'lum"
#     print(f"{rang.title()} {avto['model'].title()}, {avto['korobka']} korobka. Narhi: {narh}")

# def make_person(name, surname, year, place, email, phone):
#     return {'name': name,
#             'surname': surname,
#             'year': year,
#             'age': 2022 - int(year),
#             'place': place,
#             'email': email,
#             'phone': phone}

# people = []
# while True:
#     print("Quyidagi ma'lumotlarni kiriting:")
#     ism = input("Ism: ")
#     familiya = input("Familiya: ")
#     t_yil = input("Tug'ilgan yil: ")
#     t_joy = input("Tug'ilgan joy: ")
#     email = input("E-mail: ")
#     tel = input("Telefon raqam: ")
#     people.append(make_person(ism, familiya, t_yil, t_joy, email, tel))
    
#     javob = input("Yana odam qo'shasizmi? (yes/no): ")
#     if javob == 'no': break

# for person in people:
#     print(f"\n{person['year'].title()}-yilda {person['place'].title()}da tug'ilgan {person['name'].title()} {person['surname'].title()} {person['age']} yoshda, emaili {person['email']} va telefon raqami {person['phone']}")

# def find_prime_numbers(min, max):
#     tub_sonlar = []
#     for i in range(min, max + 1):
#         tub = True
#         if i == 1:
#             tub = False
#         elif i == 2:
#             tub = True
#         else:
#             for j in range(2, i):
#                 if(i % j == 0):
#                     tub = False
#         if tub:
#             tub_sonlar.append(i)
#     return tub_sonlar
            
# print(find_prime_numbers(1, 20))

# def return_fibonacci(num):
#     fibonacci_nums = []
#     for i in range(num):
#         if i == 0 or i == 1:
#             fibonacci_nums.append(1)
#         else:
#             fibonacci_nums.append(fibonacci_nums[i-1] + fibonacci_nums[i-2])
#     return fibonacci_nums

# print(return_fibonacci(10))

# def bahola(ismlar):
#     baholar = {}
#     while(ismlar):
#         ism = ismlar.pop()
#         baho = input(f"Talaba {ism.title()}ning bahosini kiriting: ")
#         baholar[ism] = int(baho)
#     return baholar

# talabalar = ['ali', 'vali', 'behzod', 'otabek']
# print(bahola(talabalar[:]))
# print(talabalar)

# def summa(*sonlar):
#     yigindi = 0
#     for son in sonlar:
#         yigindi += son
#     return yigindi

# print(summa(2, 3, 4))
# print(summa(7, 13, 42, 56, 3))

def avto_info(kompaniya, model, **malumotlar):
    malumotlar['kompaniya'] = kompaniya
    malumotlar['model'] = model
    return malumotlar

print(avto_info("GM", "malibu", rang="qora", yil=2018))
print(avto_info("KIA", "k5", rang="qizil", narh=35000, yil=2018))
