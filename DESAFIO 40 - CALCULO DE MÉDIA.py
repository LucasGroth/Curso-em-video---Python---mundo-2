#Um programa que leia duas notas de um aluno e calcule a sua média, mostrando uma mensagem no final, de acordo
# com a média atingida:
#Média abaixo de 5.0 = reprovado
#Média entre 5.0 e 6.9 = recuperação
#Média 7.0 ou superior: aprovado
notaa=float(input('Digite a primeira nota do aluno?'))
notab=float(input('Digite a segunda nota do aluno?'))
media=(notaa+notab)/2
if media < 5:
    print('O aluno foi reprovado!')
elif media >=5 and media <=6.9:
    print('O aluno está de recuperação!')
else:
    print('O aluno foi aprovado!')
