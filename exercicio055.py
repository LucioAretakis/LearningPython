'''lista = []

for c in range(0, 5):
    peso = float(input('Peso da {}ª pessoa: ' . format(c+1)))
    lista += [peso]
print('O maior peso foi de {} e o menor de {} '. format(max(lista), min(lista)))'''

maior = 0
menor = 0
for p in range(1,6):
    peso = float(input('Peso da {}ª pessoa: '.format(p+1)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso foi de {}Kg.'.format(maior))
print('O menor peso foi de {}Kg.'.format(menor))