#Um programa que leia dois nº INTEIROS e compare-os, mostrando na tela uma mensagem:
#-O primeiro valor é o maior.
#-O segundo valor é o maior.
#-Não existe valor maior, os dois são iguais.
import time
n1=int(input('Digite um numero inteiro: '))
n2=int(input('Digite outro numero inteiro: '))
print('Analisando números inteiros')
#AQUI QUERO A BARRA DE LOADING COM ▬
#total = 10
#for i in range(total + 1):
#   barra = '▬' * i
#    print( f'\r[{barra:<10}]', end='')
#    time.sleep(0.2)
#print('\n Resultado:')
if n1>n2:
    print('{} é o maior número e {} é o menor número.'.format(n1,n2))
elif n2>n1:
    print('{} é o maior número e {} é o menor.'.format(n2,n1))
else:
    print('Não existe número menor ou maior, os numeros informados tem o mesmo valor.')
