#Um programa para aprovar o emprestimo bancário para a compra de uma casa, O programa vai perguntar o valor da casa
#o salário do comprador e em quantos anos ele vai pagar.
#Calcule o valor da parcea mensal, sabendo que ela não pode exceder 30%
#do salário ou então o empréstimo será negado.
casa=float(input('Digite o valor da casa: '))
salario=float(input('Digite o valor do seu salário: '))
anos=int(input('Digite quantos anos deseja pagar: '))
parcela= casa/(anos*12)
maximo= salario*0.30
if parcela<=maximo:
    print('Parabéns, seu empréstimo foi aprovado!')
else:
    print('Empréstimo negado, mas não fique triste você pode tentar novamente se aumentar o tempo de pagamento!')
