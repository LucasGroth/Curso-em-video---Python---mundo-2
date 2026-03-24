#Um programa que leia um numero e diga se ele é ou não um número primo.
#Numero primo é divisivel apenas por 1 e por ele mesmo, 7 por exemplo.
r=0
n=int(input('Informe um numero inteiro:'))
for c in range(1,n+1):
    if n%c==0:
        r+=1
if r==2:
    print('É primo')
else:
    print('Não é primo!')
