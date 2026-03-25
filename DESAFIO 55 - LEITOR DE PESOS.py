#Um programa que leia o peso de 5 pessoas, no final mostre qual foi o maior e qual foi o menor peso lido.
maior=0
menor=1000
for c in range(0,5):
    peso=int(input('Digite o seu peso: '))
    if peso>maior:
        maior=peso
    elif peso<menor:
        menor=peso
print('Dos cinco pesos informados, o maior foi {}, e o menor foi {}.'.format(maior,menor))