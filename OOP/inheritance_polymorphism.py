# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 18:36:42 2022

@author: MuhammadAkbar
"""

class Shaxs:
    def __init__(self, ism, familiya, passport, tyil):
        self.ism = ism
        self.familiya = familiya
        self.passport = passport
        self.tyil = tyil
        
    def get_info(self):
        info = f"{self.ism.title()} {self.familiya.title()} {self.tyil}-yilda tug'ilgan, "
        info += f"passporti : {self.passport}"
        return info
    
    def get_age(self, yil):
        return yil - self.tyil
    
# inson = Shaxs("Akbar", "Ahmadjonov", "AB5479708", 2000)
# print(inson.get_info())
# print(inson.get_age(2022))

# Talaba klassi Shaxs super klassdan voris olyapti
class Talaba(Shaxs):
    def __init__(self, ism, familiya, passport, tyil, idraqam):
        super().__init__(ism, familiya, passport, tyil)
        self.idraqam = idraqam
        self.bosqich = 1
        
    def get_id(self):
        return self.idraqam
    
    def get_bosqich(self):
        return self.bosqich
    
    def get_info(self):
        info = f"{self.ism.title()} {self.familiya.title()} {self.tyil}-yilda tug'ilgan, "
        info += f"passporti : {self.passport}, {self.bosqich}-bosqich va id raqami : {self.idraqam}"
        return info

talaba1 = Talaba("Ali", "Valiyev", "AA8903478", 1996, "N0000011")
print(talaba1.get_id())
print(talaba1.get_age(2022))
print(talaba1.get_info())
