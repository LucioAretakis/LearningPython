from datetime import date
genero = str(input('Insira seu gênero: '))
if genero == 'Masculino':
    print('Seu alistamento é obrigatório. ')
    atual = date.today().year
    nasc = int(input('Em qual ano você nasceu? '))
    idade = atual - nasc
    if idade == 18:
        print('Está na hora de se alistar!')
    elif idade > 18:
        saldo = idade - 18
        prazo = atual - saldo
        print('Você deveria ter se alistado há {} anos.'.format(saldo))
        print('Seu ano de alistamento foi em {}.'.format(prazo))
    else:
        saldo = 18 - idade
        prazo = atual + saldo
        print('Você está a {} anos de se alistar.'.format(saldo))
        print('Seu alistamento será no ano de {}.'.format(prazo))
elif genero == 'Feminino':
    print('Seu alistamento não é obrigatório')
