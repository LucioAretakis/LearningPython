from datetime import date
ano = int(input('Ano de nascimento: '))
idade = date.today().year - ano
print('você tem {} anos'.format(idade))
if idade <= 9:
    print('Você é um nadador MIRIM.')
elif idade <= 14:
    print('Você é um nadador INFANTIL.')
elif idade <= 19:
    print('Você é um nadador JUNIOR.')
elif idade <= 25:
    print('Você é um nadador SÊNIOR')
else:
    print('Você é um nadador MASTER.')