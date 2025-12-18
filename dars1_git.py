# def out(x):
#     def into(z):
#         return x+z
#     return  into
# add_five=out(5)
# print(add_five(5))
from importlib.metadata import pass_none
from itertools import count

# def pasword():
#     standart=111222
#     def tekshirish(x):
#         if x<=standart:
#             return f"mayli ma qariz senga!!! "
#         else:
#             return f"szga qariz bermiman"
#     return tekshirish
#
# a=int(input("summani yoz: "))
# pasword()


# def matin(matn):
#     def clean():
#         return matn.strip().lower()
#     def longer():
#         return matn.count("a")
#
#     def short():
#         new=matn.split()
#         new=[len(i) for i in new]
#         print(sum(new))
#         return sum(new)
#
#     matn=data.clean()
#
#     return clean(),longer(),short()
#
# print(matin(" salom  A DUNYO! "))


# def hisoblagich():
#     son=0
#     def qoshish():
#         nonlocal son            #4653214653565
#
#     return qoshish()

# def log(z):
#     print("funk is going! ")
#     z()
#     print("funk is end!")
# def salom():
#     print("hello world")
# log(salom)
#
# for q in range(3):
#     for i in range(1, 10):
#         if i == 4:
#             continue
#         else:
#             print(i, end=" ")
#     print()

# =========================================

# def out_sum():
#     qarz=100000
#     def inside(out):
#         if out<=qarz:
#             return f"ma senga pul"
#         else:
#             return f"senga pul yoq"
#     return  inside
#
# lol=out_sum()
# print(lol(90))


# def tashqi():
#     son=0
#     def ichki():
#         nonlocal son
#         son+=1
#         if son==3:
#             son=1
#         return son
#     return ichki
# l=tashqi()
# print(l())
# print(l())
# print(l())
# print(l())


# class Student:
#     def __init__(self,name,grade):
#         self.name=name
#         self.grade=grade
#
#     def __eq__(self, other):
#         return  self.grade==other.grade
#
#     def __next__(self,x):
#         return self.grade!=x.grade
#
#     def __lt__(self, other):
#         return  self.grade<other.grade
#
#     def __le__(self, other):
#         return  self.grade<=other.grade
#
#     def __gt__(self, other):
#         return  self.grade>other.grade
#
#     def __ge__(self, other):
#         return  self.grade>other.grade
#
# s1=Student("ali",78)
# s2=Student("vali",34546)
#
# print(s1==s2)
# print(s1!=s2)
# print(s1<s2)

#
# class Student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#
#     def get(self):
#         return f"{self.name} ning yoshi {self.age}"
#
#     def __eq__(self, other):
#         if isinstance(other,Student):
#             return self.name==other.name and self.age==other.age
#
#     def __hash__(self):
#         return hash((self.name,self.age))
#
# obj=Student("java",19)
# obj2=Student("lava",19)
# obj3=Student("ali",20)
#
# print(obj)
# print(obj3)

