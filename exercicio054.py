from datetime import date

ano = date.today().year
maior = 0
menor = 0
for c in range(0, 7):
    nasc = int(input('Insira seu ano de nascimento: '))
    idade = ano - nasc
    if idade >= 18:
        maior += 1
    else:
        menor += 1
print('{} PESSOAS JÁ ATINGIRAM A MAIORIDADE, E {} AINDA NÃO.'.format(maior, menor))
