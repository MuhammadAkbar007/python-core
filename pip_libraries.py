# -*- coding: utf-8 -*-
"""
Created on Sat Jun 25 19:54:26 2022

@author: MuhammadAkbar
"""

# from googletrans import Translator

# tarjimon = Translator()

# matn_uz = "Python dasturlash tilini o'rganyapman !"

# tarjima = tarjimon.translate(matn_uz)
# print(tarjima.origin) #original matn
# print(tarjima.text) #tarjima matni
# print(tarjima.src) #original matn tili

# tarjima_ru = tarjimon(matn_uz, dest = 'ru') #destination russian
# print(tarjima_ru.text)

import requests
from pprint import pprint

sahifa = "https://kun.uz/news/main"

r = requests.get(sahifa)
pprint(r.text)