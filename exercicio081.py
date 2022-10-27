valores = []
cont = 0
while True:
    valores.append(int(input('Digite o valor a ser adicionado na lista: ')))
    cont += 1
    resp = input('Você deseja continuar? ').strip().upper()[0]
    while resp not in 'SN':
        resp = input('Resposta inválida, responda com S ou N').strip().upper()[0]
    if resp in 'N':
        break


print(f'foram adicionados {cont} valores na lista')
print(f'A lista em ordem decrescente ficou {sorted(valores, reverse = True)}')
if 5 in valores:
    print(f'O valor 5 se encontra na lista na posição {valores.index(5)}')
else:
    print('O valor 5 não foi inserido na lista')