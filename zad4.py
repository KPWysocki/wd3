def monoton(y,x,b):
    A = (y-b)/x
    if (A<0):
        print("Funkcja malejaca")
    elif (A==0):
        print("Funkcja stała")
    elif (A>0):
        print("Funkcja rosnąca")
    return 0


y = int(input())
x = int(input())
b = int(input())

A=monoton(y,x,b)