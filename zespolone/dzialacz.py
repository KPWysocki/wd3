A=complex(input())
B=complex(input())
sumaReal=(A.real+B.real)
sumaImag=(A.imag+B.imag)
print('Suma liczb zespolonych wynosi: ', end='')
print(sumaReal, end='')
print('+', end='')
print(sumaImag, end='')
print('i')
rozReal=(A.real-B.real)
rozImag=(A.imag-B.imag)
print('Roznica liczb zespolonych wynosi: ', end='')
print(rozReal, end='')
print('+', end='')
print(rozImag, end='')
print('i')