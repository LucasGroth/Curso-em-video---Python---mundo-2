#Refaça o desafio 35 dos triangulos, acrescentando o recurso de mostrar que tipo de triangulo será formado:
#equilátero(lados iguais) / Isóceles (dois lados iguais) / Escaleno ( Todos os lados diferentes)
retaa=float(input('Digite o tamanho da primeira reta:'))
retab=float(input('Digite o valor da segunda reta:'))
retac=float(input('Digite o valor da terceira reta:'))
if retaa+retab>retac and retaa+retac>retab and retab+retac>retaa:
    print('Forma um triangulo')
    if retaa==retab==retac :
        print('o triangulo formado é um triangulo equilátero, pois, tem todas as retas do mesmo tamanho.')
    elif retaa==retab or retaa==retac or retac==retab :
        print('O triangulo formado é um triangulo isóceles pois tem duas retas do mesmo tamanho.')
    else:
        print('O triangulo formado é do tipo escaleno, pois todos os lados tem medidas diferentes.')
else:
    print('Não forma um triangulo.')
