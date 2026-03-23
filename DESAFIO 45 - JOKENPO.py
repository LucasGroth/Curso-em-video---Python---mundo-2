#Crie um programa que faça o computador jogar jokenpô com você.
from random import choice
lista=['pedra','papel','tesoura']
cpu=choice(lista)
player=(input('Vamos jogar JOKENPÔ ! \n Eu já fiz minha escolha, qual é a sua ?')).strip().lower()
if cpu==player:
    print('Empatamos!')
elif cpu=='pedra' and player=='papel' or cpu=='papel' and player =='tesoura' or cpu=='tesoura' and player=='pedra':
    print('Parabéns, você venceu!')
else:
    print('Eu venci, mais sorte na próxima!')