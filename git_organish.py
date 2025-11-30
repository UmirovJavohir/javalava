# rows==строка
# columns==столбец
# symbol==символ

stroka=int(input("введите кол-во строк: "))
stolbets=int(input("введите кол-во столбец: "))
symvol=input("введите кол-во символ: ")

for q in range(stroka):
    for w in range(stolbets):
        print(symvol, end=" ")
    print()