#Um programa que leia nome, idade e sexo de 4 pessoas.No final no programa mostre:
#A média de idade do grupo ; Qual o nome do homem mais velho; Quantas mulheres tem menos de 20 anos.
somaidade=0
nomevelho=''
idadevelho=0
mulheres=0
mulherjovem=0
for c in range(0,4):
    nome=str(input('Digite seu nome: '))
    idade=int(input('Digite sua idade: '))
    sexo=str(input('Digite seu sexo(M ou f): ')).strip().upper()
    somaidade= idade+somaidade
    if sexo=='M':
        if idade>idadevelho:
            idadevelho=idade
            nomevelho=nome
    elif sexo=='F':
        mulheres+=1
        if idade<20:
            mulherjovem+=1
media=somaidade/4
print('Das quatro pessoas registradas,o nome do homem mais velho é {}, ele tem {} anos, no grupo há {} mulheres,'
      'sendo {} delas, menor de 20 anos, a idade média das pessoas registradas é {}.'
      .format(nomevelho,idadevelho,mulheres,mulherjovem,media))