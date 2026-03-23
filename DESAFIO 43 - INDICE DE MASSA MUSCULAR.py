#Um programa que leia o peso e a altura de uma pessoa.Calcule seu ICM e mostre seu status, de acordo com a tabela abaixo:
#Abaixo de 18.5: abaixo do peso / Entre 18.5 e 25: peso ideal / 26 a 30 sobrepeso
#30 a 40 obesidade / acima de 40 obsediade mórbida
nome=input('Qual o seu nome? ')
print('Seja bem vindo {}, vou calcular seu ICM hoje, para isso preciso de algumas informações:'.format(nome))
peso=float(input('Qual o seu peso? '))
altura=float(input('Qual a sua altura? '))
print('Calculando...')
icm=peso/altura**2
if icm< 18.5:
    print('Você está abaixo do peso ideal.')
elif icm>=18.5 and icm<=25:
    print('Você está no peso ideal.')
elif icm>25 and icm<=30:
    print('Você está com sobrepeso.')
elif icm>30 and icm<=40:
    print('Você está com obesidade.')
else:
    print('Você está com obesidade mórbida.')