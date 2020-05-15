import math
def promien(a,b):
    x=0
    y=0
    R=((x-a)*(x-a))-((y-b)*(y-b))
    r=math.sqrt(R)
    print(r)
    return 0

a=int(input())
b=int(input())
r=promien(a,b)