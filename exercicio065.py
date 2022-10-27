cont = soma = menor = maior = 0
resp = ' '
while True:
    n = int(input("VALOR: "))
    cont += 1
    soma += n
    media = soma / cont
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n
    resp = input("VOCÊ DESEJA CONTINUAR? ").upper().strip()[0]
    if resp in 'Nn':
        break

print(f'A média de todos os valores inseridos foi {media:.2f}')
print(f'o maior valor foi  {maior} e o menor {menor}')


