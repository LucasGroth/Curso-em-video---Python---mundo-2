#Um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade:
#Se ele ainda vai se alistar / Se é a hora de se alistar / Se já passou da hora de se alistar
#O programa também deverá mostrar o tempo que falta ou passou do prazo.
from datetime import datetime
nascimento=int(input('Qual seu ano de nascimento? '))
ano= datetime.now().year
idade=ano-nascimento
if idade==18:
    print('Chegou a hora de se alistar!')
elif idade<18:
    print('Ainda não está na hora de se alistar, ainda faltam {} anos para você fazer seu alistamento!'.format(18-idade))

else:
    print('Já passou da hora de se alistar, você deve regularizar sua situação!\nSeu alistamento está atrasado já a {} anos!'.format(idade-18))
