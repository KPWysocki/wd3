import numpy as np
A=np.random.randint(10, size=(4,4))
print(A)
B=[A[0,0], A[1,1],A[2,2],A[3,3]]
C=[A[0,3], A[1,2],A[2,1],A[3,0]]
print(B)
print(C)