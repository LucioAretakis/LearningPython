preco = float(input('Qual o valor do produto? '))
formas = ('', 'à vista no dinheiro', 'à vista no cartão', 'em até 2x no cartão', 'em 3x ou mais no cartão')
print(''''Os métodos de pagamento são os a seguir
[1] á vista no dinheiro
[2] á vista no cartão
[3] em até 2x no cartão
[4] em 3x ou mais no cartão''')
pagamento = int(input('Qual será o método de pagamento? '))
if pagamento == 1:
    valor = preco - 10/100*preco
    print('O valor total ficará R${}.'.format(valor))
elif pagamento == 2:
    valor = preco - 5/100*preco
    print('O valor total ficará R${}.'.format(valor))
elif pagamento == 3:
    valor = preco
    parcela = preco / 2
    print('O valor total ficará R${:.2f}. Você irá pagar duas parcelas de R${:.2f}. ' .format(preco, parcela))
elif pagamento == 4:
    valor = preco + 20/100*preco
    totparc = int(input('Em quantas parcelas você deseja pagar o produto? '))
    parcela = valor / totparc
    print('Sua compra será parcelada em {}x, e cada parcela custará R${:.2f}.'. format(totparc, parcela))
else:
    valor =preco
    print('Opção inválida.')
    print('O valor total ficará R${}.'.format(valor))
