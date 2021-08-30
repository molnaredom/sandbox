

import random as r

kitalalando = r.randint(1, 100)

while True:

    a = int(input("addj meg egy szamot 1-100ig hogy szukitsd az intervellunot: "))

    if a<kitalalando:
        print(a, "< x")
    elif a>kitalalando:
        print(a,"> x")
    else:
        print("megtalalva yeey")
        break








