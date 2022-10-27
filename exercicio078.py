valores = list()
maior = menor = 0
for c in range(0,5):
    valores.append(int(input(f'Insira um valor na posição {c}: ')))
    if c == 0:
        maior = menor = valores[c]## o maior e o menos numero são os inseridos na posição 0 da lista
    else:
        if valores[c] > maior:
            maior = valores[c]
        if valores[c] < menor:
            menor = valores[c]
print(f'O maior valor da lista é {maior} nas posições ', end= '')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}...', end= '')
print( )
print(f'O menor valor da lista é {menor} nas posições ', end= '')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}...', end= '')
