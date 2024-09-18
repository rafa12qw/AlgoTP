from random import * # chargement de toute la bibliotheque
from matplotlib import pyplot as plt # chargement d ’ un des modules de matplotlib
from math import*

def entiersAletoires(n,a,b):
    T = [randint(a,b) for _ in range(n)]
    return T


def entiersAletoires2(n,a,b):
    T = [randrange(a,b) for _ in range(n)]
    return T 

def flottantAletoires(n):
    T = [random() for _ in range(n)]
    return T 

def flottantAletoires2(n,a,b):
    T = [uniform(a,b) for _ in range(n)]
    return T 


#3.
def pointDisque(n):
    D = []
    i=0
    while i < n:
        x = uniform(-1,1)
        y = uniform(-1,1)
        
        z = x**2+y**2
        if z <= 1:
            D.append([x,y])
            i+=1
    return D

def pointDisque2(n):
    D = []
    i = 0

    while i < n:
        x = uniform(-1,1)
        y = uniform(-1,1)

        z = x**2 +y**2
        while z > 1:
            y = uniform(-1,1)
            z = x**2 +y**2
        D.append([x,y])
        i+=1
    return D

def pointDisque3(n):
    D = []
    for i in range(n):

        theta = uniform(0,2*pi)
        r = uniform(0,1)
        D.append([r*cos(theta),r*sin(theta)])
    return D

def affichagePoints ( L ):
    X = [ x for x , y in L ] # on recupere les abscisses ...
    Y = [ y for x , y in L ] # ... et les ordonnees
    plt.scatter (X,Y, s = 1) # taille des points minimale
    plt.axis ("square") # meme echelle en abscisse et ordonnee
    plt.show()

#4.

def aletoireModulo(N):
    k = N.bit_length()
    x = getrandbits(k)
    return x % N

def aletoireRejet(N):
    k = N.bit_length()
    x = 0
    while x > N:
        x = getrandbits(k)
    return x % N

    
def main():
    L1=entiersAletoires(1000,1,100)
    L2=entiersAletoires2(1000,1,100)
    #plt.hist(L1,bins=100)
    #plt.hist(L2,bins=100)
    #plt.show()
    L1 = flottantAletoires(1000)
    L2 = flottantAletoires2(1000,-3,10)

    #plt.plot(L1)
    #plt.plot(L2)
    #plt.show()

    L1 = pointDisque(100000)
    L2 = pointDisque2(100000)
    L3 = pointDisque3(100000)

    #affichagePoints(L1)
    #affichagePoints(L2)
    #affichagePoints(L3)
    T1 = []
    T2 = []
    for i in range(10000):
        T1.append(aletoireModulo(100))
        T2.append(aletoireRejet(100))
    plt.hist(T1,bins=100)
    plt.hist(T2,bins=100)
    plt.show()
    

if __name__ == "__main__":
    main()
