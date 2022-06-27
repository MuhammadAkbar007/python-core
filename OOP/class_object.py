# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 13:53:42 2022

@author: MuhammadAkbar
"""

class Talaba:
    def __init__(self, ism, familiya, tyil):
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil
        self.bosqich = 1
        
    def tanishtir(self):
        return f"Kamina {self.ism.title()} {self.familiya.title()} {self.tyil}-yilda tug'ilganman !"

    def get_name(self):
        return self.ism
    
    def get_age(self, yil):
        return yil - self.tyil
    
    def get_fullname(self):
        return f"{self.ism} {self.familiya}"
    
    def see_methods(klass):
        return [method for method in dir(klass) if method.startswith('__') is False]

talaba1 = Talaba("Olim", "Olimov", 2000)

print(talaba1.__dict__)
print(talaba1.__dict__.keys())
print(talaba1.__dict__.values())

class Fan:
    def __init__(self, nomi):
        self.nomi = nomi
        self.talabalar_soni = 0
        self.talabalar = []

    def add_student(self, talaba):
        self.talabalar.append(talaba)
        self.talabalar_soni += 1

    def get_students(self):
        return [talaba.get_fullname() for talaba in self.talabalar]

matem = Fan("Oliy matematika")