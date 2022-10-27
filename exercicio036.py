valor = float(input('Qual o valor da casa desejada? '))
salario = float(input('Qual o salário que você recebe? '))
anos = int(input('Em quantos anos você deseja pagar? '))
prestacao = valor / (anos*12)
print('Para você comprar uma casa de R${:.2f} em {} anos'.format(valor, anos), end='')
print(' o valor da prestação será de R${:.2f}.'.format(prestacao))
if prestacao >= 30/100 * salario:
    print('Nós não podemos liberar o empréstimo para você comprar a casa.')
else:
    print('Seu empréstimo será liberado em até 15 dias.')

