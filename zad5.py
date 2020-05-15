def rownol(y1,x1,b1,y2,x2,b2):
    A1 = (y1-b1)/x1
    A2 = (y2-b2)/x2
    if (A1==A2):
        print("Równoległe")
    elif (A1*A2==-1):
        print("Funkcja stała")
    return 0


y1 = int(input())
x1 = int(input())
b1 = int(input())
y2 = int(input())
x2 = int(input())
b2 = int(input())

A=rownol(y1,x1,b1,y2,x2,b2)