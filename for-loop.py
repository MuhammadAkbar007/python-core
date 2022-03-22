# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 15:18:29 2022

@author: MuhammadAkbar
"""

# mehmonlar = ['Ali','Vali','Hasan', 'Husan','Olim']

# for mehmon in mehmonlar:
#     print('Salom', mehmon) 
#     print('Hayr', mehmon)

# sonlar = list(range(1, 11))
# for son in sonlar:
#     print(f"{son} ning kvadrati = {son**2}")

friends = []
print('5 ta eng yaqin do\'singizni tanlang !!!')
for i in range(5): # 0, 1, 2, 3, 4 marta sikl aylanishini ta'minlaydi
    friends.append(input(f"{i+1}-do'stingiz ismini kiriting >>> "))
print(f"Sizning eng yaqin do'stlaringiz: {friends}")