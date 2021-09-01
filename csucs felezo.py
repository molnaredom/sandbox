

import random

a = [random.randint(1,10) for i in range(int(input("add meg hany szam legyen a tombben")))]

print(a)
lo = 1
hi = len(a) - 2
def iterativ():
    global lo
    global hi
    while lo <= hi:
        mid =int( lo + (hi - lo) / 2)

        if a[mid]  < a[mid-1]:
            hi = mid - 1
        elif a[mid] < a[mid +1]:
            lo = mid +1
        else:
            return mid

print(iterativ())



def find_a_peak_in(lista, lo, hi):
    if (hi-lo <= 1):
        return lo
    if lista[lo] >= lista[lo +1]:
        return lo
    if lista[hi] >= lista[hi-1]:
        return hi

    mid = lo + (hi - lo) /2
    if lista[mid] < lista[mid -1]:
        return find_a_peak_in(lista,lo,mid-1)
    elif lista[mid] < lista[mid +1]:
        return find_a_peak_in(lista,mid+1,hi)
    return mid

print(find_a_peak_in(a,lo,hi))




