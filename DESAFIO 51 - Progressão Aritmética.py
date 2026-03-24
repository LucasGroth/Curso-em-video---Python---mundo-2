#Um programa que leia o primeiro termo e a razão de uma PA. E mostre os 10 primeiros termos dessa PA.
i = int(input('Informe o primeiro termo da progressão: '))
r = int(input('Informe a razão desejada para essa PA: '))
for c in range(10):
    print(i + c * r)

## JEITO QUE EU CONSEGUI MAS TEM UM PROBLEMA SE A RAZÃO FOR NEGATIVA :
i=int(input('Informe o primeiro termo da progressão:'))
r=int(input('Informe a razão desejada para essa PA:'))
for c in range(i,i+r*10,r):
    print(c)
