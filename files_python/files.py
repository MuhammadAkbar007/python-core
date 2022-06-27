# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 00:24:43 2022

@author: MuhammadAkbar
"""

# file = open('pi.txt')
# PI = file.read()
# print(PI)
# file.close()

# with open('pi.txt') as file:
#     pi = file.read()
    
# print(pi)
# pi = pi.rstrip()
# pi = pi.replace('\n', '')
# pi = float(pi)
# print()
# print(pi)

# filename = 'data/talabalar.txt'
# with open(filename) as file:
#     for line in file:
#         print(line)

# with open(filename) as file:
#     talabalar = file.readlines()
    
# talabalar = [talaba.rstrip() for talaba in talabalar]
# print(talabalar)

# faylnomi = 'new_file.txt'
# ism = 'Olimjon Husanov'
# tyil = 1994
# with open(faylnomi, 'w') as fayl: # write => ustidan yozish
#     fayl.write(ism + '\n')
#     fayl.write(str(tyil) + '\n')

# with open(faylnomi, 'a') as fayl: # append => davomidan yozish
#     fayl.write('Alijon Valiyev \n')
#     fayl.write('2000')

import pickle

# talaba1 = {'ism': 'hasan', 'familiya': 'husanov', 'tyil': 2003, 'kurs': 2}
# talaba2 = {'ism': 'alijon', 'familiya': 'valiyev', 'tyil': 2004, 'kurs': 1}

# with open('info.pkl', 'wb') as file: # write binary => binar ko'rinishda yozadi
#     pickle.dump(talaba1, file)
#     pickle.dump(talaba2, file)

with open('info.pkl', 'rb') as file: # read binary => binar o'qish
    talaba1 = pickle.load(file)
    talaba2 = pickle.load(file)
    
print(talaba1)
print(talaba2)
