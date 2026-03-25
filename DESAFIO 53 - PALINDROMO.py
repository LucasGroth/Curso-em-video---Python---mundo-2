#Um programa que leia uma frase qualquer e diga se ela é ou não um palíndromo.
frase=input('Digite uma frase: ').lower()
semespaço=frase.replace(' ','')
invertida = ''
for letra in semespaço:
    invertida = letra + invertida
if invertida == semespaço:
    print('A frase é um palíndromo.')
else:
    print('A frase não é um palíndromo.')
