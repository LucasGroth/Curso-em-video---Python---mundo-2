#Um programa que mostre a taboada do número que o usuário pedir:
n=int(input('Qual número você quer saber a taboada?'))
for c in range(1,11):
    print('{}x{}={}'.format(n,c,n*c))