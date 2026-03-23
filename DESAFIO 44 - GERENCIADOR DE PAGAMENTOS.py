#Um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal,
#e a condição de pagamento:
#A vista dinheiro = 10% de desconto
#A vista no cartão = 5% de desconto
#Em até 2 vezes no cartão: preço normal
#3 ou mais vezes no cartão: 20% de juros
valorinicial=float(input('Digite o valor inicial do produto: '))
formaDePagamento=input('Digite a forma de pagamento:\n 1)A vista no dinheiro. \n 2) A vista no cartão. \n 3)2 vezes no cartão. \n 4)3 vezes ou mais no cartão. ').strip().upper()
if formaDePagamento=='1':
    print('Voce recebeu 10% de desconto, então o produto custará R$ {:.2f}.'.format(valorinicial*0.9))
elif formaDePagamento=='2':
    print('Você recebeu 5% de desconto, e o produto custará R$ {:.2f}.'.format(valorinicial*0.95))
elif formaDePagamento=='3':
    print('Com essa forma de pagamento não há alteração no preço do produto, ficará R${:.2f}.'.format(valorinicial))
elif formaDePagamento=='4':
    print('Para pagamentos no cartão em 3 vez ou mais, cobramos uma taxa de juros de 20%, o produto custará R${:.2f}.'.format(valorinicial+valorinicial*0.2))
else:
    print('Tente novamente!')
