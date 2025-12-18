# 1. Transport vositalari tizimi
# Shart: Transport vositalari uchun Vehicle nomli asosiy klass yarating. Undan voris oluvchi Car, Bicycle, va Truck klasslarini hosil qiling.
# Vehicle klassi umumiy atributlarga ega bo‘lsin: name, speed.
# Car, Bicycle, Truck klasslari har biri o‘ziga xos metodlarga ega bo‘lsin (honk(), load_cargo(), pedal()).
# Ma’lumot: Masalan, Car obyektida honk() metodidan foydalansa, "Bip-bip!" degan natija chiqishi kerak.
from math import trunc
from turtledemo.penrose import makeshapes


#
# class Vehicle:
#     def __init__(self, name,speed):
#         self.name=name
#         self.speed=speed
#
# class Car(Vehicle):
#     def honk(self):
#         return "Bip-bip!"
#
# class Moto(Vehicle):
#     def load_cargo(self):
#         return "qoch yoldan! tirancha ┗|｀O′|┛ "
#
# class Truck(Vehicle):
#     def pedal(self):
#         return "tormoz ishlamayabti qoch yoldan YIBALAY BILLLLLLeT=CHIPTA "
# #
#
# car=Car("onix",130)
# print(car.honk())
#
# moto=Moto("mitsubishi",2345643420)
# print(moto.load_cargo())
#
# truck=Truck("dalnoboy",100)
# print(truck.pedal())



# 2. Hayvonot bog‘i tizimi
# Shart: Hayvonlarni ifodalovchi Animal nomli asosiy klass yarating. Undan voris oluvchi Lion, Eagle, va Shark klasslarini hosil qiling.
# Animal klassida umumiy metodlar bo‘lsin (make_sound()).
# Lion, Eagle, Shark klasslari make_sound() metodini o‘ziga xos tarzda o‘zgartirsin (roar(), screech(), splash()).
# Ma’lumot: Masalan, Lion obyektida make_sound() metodini chaqirsak, natija "Roar!" bo‘lishi kerak.

# class Animal:
#     def make_sound(self):
#         pass
#
# class Lion(Animal):
#     def make_sound(self):
#         return "lion can run fast"
#
# class Eagle(Animal):
#     def make_sound(self):
#         return "eagle can fly above then 100m"
#
# class Shark(Animal):
#     def make_sound(self):
#         return "shark can swim"
#
# lion=Lion()
# print(lion.make_sound())
#
# eagle=Eagle()
# print(eagle.make_sound())
#
# shark=Shark()
# print(shark.make_sound())


# 3.Ishchilar boshqaruvi tizimi
# Shart: Ishchilarni ifodalovchi Employee nomli asosiy klass yarating. Undan voris oluvchi Manager, Developer, va Designer klasslarini hosil qiling.
# Employee klassida umumiy metod bo‘lsin: get_salary().
# Manager, Developer, Designer klasslari har biri o‘zining alohida maosh hisoblash usuliga ega bo‘lsin.
# Ma’lumot: Masalan, Developer klassining get_salary() metodi maoshni hourly_rate * hours_worked shaklida qaytarsin.

# class Employee:
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary
#
# class Manager(Employee):
#     def get_salary(self):
#         return  f"Имя менеджера: {self.name}, зарплата=> {self.salary}"
#
# class Developer(Employee):
#     def get_salary(self):
#         return f"Имя разработчика: {self.name}, зарплата=> {self.salary}"
#
# class Designer(Employee):
#     def get_salary(self):
#         return f"Имя дизайнера: {self.name}, зарплата=> {self.salary}"
#
# manager=Manager("Javohir",1234567)
# print(manager.get_salary())
#
# devol=Developer("Shohrux",1234567)
# print(devol.get_salary())
#
# disayner=Designer("Saidislom",31245632)
# print(disayner.get_salary())