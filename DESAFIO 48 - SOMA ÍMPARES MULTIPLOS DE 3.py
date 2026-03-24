#Um programa  que calcule a soma  entre todos os números ímpares que são multiplos de 3 no intervalo de 1 a 500.
s=0
for c in range(1+2,500,3):
    s+=c
    print(c)
print('A soma total dos multiplos de 3 no intervalo entre 1e 500 é {}.'.format(s))