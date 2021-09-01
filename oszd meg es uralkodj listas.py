import random


lista = [random.randint(1,10) for i in range(int(input("add meg hany szam legyen a tombben")))]
print(lista)

"""
kerdes hogy hogy talaljuk meg a csuscsot
mindig 2 fele osztjuk a tombot ugy hogy abba az iranyba valasztunk amerre magasabb szam van
"""
n = len(lista)

while True:

    print(lista[int((n/2))])

    

    break

