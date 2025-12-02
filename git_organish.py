# class fruits:
#     def __init__(self,title,price,quality):
#         self.name=title
#         self.narxi=price
#         self.soni=quality
#
# lol=fruits("olma",15000,10)
# print(lol.__dict__)

class fruits:
    def __init__(self,title,price,quality):
        self.name=title
        self.narxi=price
        self.soni=quality

    def fruits1(self):
        return {
            "name":self.name,
            "narxi":self.narxi,
            "soni":self.soni
        }
    def lol(self,title_1,price_1):
        self.name=title_1
        self.narxi=price_1

olma=fruits("olma",13000,10)
print(olma.fruits1())
olma.lol("banan",20000)
print(olma.fruits1())