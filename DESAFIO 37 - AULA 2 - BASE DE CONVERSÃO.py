#Escreva um programa que leia um nº inteiro qualquer e peça para o usuário
#escolher qual será a base de conversão:
#a) 1 para binário b)2 para octal c)3 para hexadecimal
n=int(input('Escreva um número inteiro qualquer'))
base=(input('Você quer esse número convertido para:\n1-Binário;\n2-Octal;\n3-Hexadecimal;\nResponda com 1,2 ou 3.').strip())
if base=='1':
    nb=bin(n)
    print('O número {} em forma binária fica {}.'.format(n,nb[2:]))
elif base=='2':
    no=octal(n)
    print('O número {} em forma octal fica {}.'.format(n,no[2:]))
elif base=='3':
    nh=hex(n)
    print('O número{} em forma hexadecimal fica {}.'.formata(n,nh[2:]))
else:
    print('Resposta invalida)')
