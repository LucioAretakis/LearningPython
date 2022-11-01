dados = list() 
maior = menor = nomemaior = nomemenor = 0
while True:
    nome = input('NOME: ')
    peso = int(input('PESO: '))
    listagem = [nome, peso]
    dados.append(listagem[:])
    if len(dados) == 0:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
            nomemaior = nome
        if peso < menor:
            menor = peso
            nomemenor = nome

    resp = ' '
    while resp not in 'SN':
        resp = input('Você deseja continuar? ').strip().upper()[0]
    if resp in 'N':
        break

print(f'{dados}')
print(f'{len(dados)} pessoas foram cadastradas')
print(f'O maior peso foi o de {nomemaior} e foi de {maior}KG ')
print(f'O menor peso foi o de {nomemenor} e foi de {menor}KG ')
