#A confederação nacional de natação precisa de um programa que leia o ano de nascimento
#de um atleta e mostre sua categoria, de acordo com a idade:
#Até 9 anos - mirim /Até 14 anos - infantil / Até 19 anos- Junior /Até 25 anos - Senior /Acima de 25 - Master
idade= int(input('Digite a idade do atleta:'))
if idade <= 9:
    print('Categoria mirim.')
elif idade >9 and idade <= 14:
    print('Categoria infantil')
elif idade >14 and idade <= 19:
    print('categoria junior.')
elif idade >19 and idade <= 25:
    print('categoria senior.')
else :
    print('categoria master.')
