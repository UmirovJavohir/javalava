def eng_kottasi(q,w,e):
    if q>w>e:
        print(f"eng kattasi: {q}")
    elif w>e>q:
        print(f"eng kattasi: {w}")
    else:
        print(f"eng kattasi: {e}")


q=int(input("1-chi sonni yozing: "))
w=int(input("2-chi sonni yozing: "))
e=int(input("3-chi sonni yozing: "))

eng_kottasi(q,w,e)