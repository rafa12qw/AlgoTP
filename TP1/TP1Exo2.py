
from random import * # chargement de toute la bibliotheque

def eltMajDet(T):
    n = len(T)
    m = n // 2

    for i in range(n):
        cpt = 0
        for j in range(i+1,n):
            if T[i] == T[j]:
                cpt += 1
        if cpt == m:
            return T[i]
    return -1

def eltMajProba(T):
    n = len(T)

    while True:
        x = choice(T)
        cpt = 0
        for i in range(n):
            if T[i] == x:
                cpt += 1
        if cpt == n//2:
            return x 
    



if __name__ == "__main__":
    main()