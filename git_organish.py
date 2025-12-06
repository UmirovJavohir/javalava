# =================================================== 1
#
# class person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#
#     def get_info(self):
#         return f"your name {self.name} and you are {self.age} years old"
#
#     @classmethod
#     def from_birth_year(cls,name,birth_year):
#         year=2025-birth_year
#         return cls(name,year)
#
# information=person(name="Javohir",age=19)
# print(information.get_info())
# answer=person.from_birth_year("dilshod",2006)
# print(answer.get_info())

# --------------------------------------------------- 2
#
# class student:
#     def __init__(self,fullname,grade):
#         self.name=fullname
#         self.grade=grade
#
#     def get_info(self):
#         return f"your name is {self.name}, you got {self.grade} grade"
#
#     @staticmethod
#     def qwerty(grade):
#         return grade>=1 and grade<=11
#
#     @classmethod
#     def create(cls,fullname,grade):
#         return cls(fullname,grade)
#
# s=student.create("Azizbek",9)
# print(s.get_info())
