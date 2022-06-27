# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 19:08:31 2022

@author: MuhammadAkbar
"""

from uuid import uuid4

class Avto:
    __num_avto = 0
    def __init__(self, make, model, rang, yil, narh, km = 0):
        self.make = make
        self.model = model
        self.rang = rang
        self.yil = yil
        self.narh = narh
        self.__km = km
        self.__id = uuid4()
        Avto.__num_avto += 1
        
    # def __str__(self):
    #     return f"Avto: {self.make} {self.model}"
        
    def __repr__(self): # toString() methodi
        return f"Avto: {self.make} {self.model}"
    
    def __eq__(self, y): # ikki obj ni teng ekanligini tekshiradi
        return self.narh == y.narh
    
    def __lt__(self, y): # birinchi obj kichikmi
        return self.narh < y.narh
    
    def __le__(self, y): # birinchi obj kichik yoki tengmi
        return self.narh <= y.narh
        
    @classmethod
    def get_num_avto(cls):
        return cls.__num_avto
        
    def get_km(self):
        return self.__km
    
    def get_id(self):
        return self.__id

    def add_km(self, km):
        if km > 0: self.__km += km
        else: print("Mashina kilometrini kamaytirib bo'lmaydi !")

avto1 = Avto("GM", "Malibu", "Qora", 2020, 40000, 1000)

class AvtoSalon:
    def __init__(self, name):
        self.name = name
        self.avtolar = []
        
    def __repr__(self):
        return f"{self.name} avtosaloni"
    
    def get_item(self, ind):
        return self.avtolar[ind]
    
    def add_avto(self, *qiymat):
        for avto in qiymat:
            if isinstance(avto, Avto): self.avtolar.append(avto)
            else: print("Avto kiriting !")