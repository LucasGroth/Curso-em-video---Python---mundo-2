#Um programa que leia a idade de 7 pessoas, no final mostre quantas delas
#atingiram a maioridade e quantas ainda não.
maioridade=0
menoridade=0
for c in range(0,7):
    idade=int(input('Digite sua idade: '))
    if idade>=18:
        maioridade=maioridade+1
    elif idade<18:
        menoridade=menoridade+1
print('Das 7 pessoas, {} são maiores de idade e {} são menores.'.format(maioridade,menoridade))