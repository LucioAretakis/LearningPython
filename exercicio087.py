valores = []
pares = soma = maior = 0
for c in range(0,3):
    num = int(input(f'digite um valor para [0,{c}]: '))
    valores.append(num) 
    if c == 2:
        for v in range(0,3):
            num = int(input(f'digite um valor para [1,{v}]: '))
            valores.append(num)
            if v == 2:
                for i in range(0,3):
                    num = int(input(f'digita um valor para [2,{i}]: '))
                    valores.append(num)
for i, n in enumerate(valores):
    if n % 2 == 0:
        pares += n

if valores[3] > valores[4] and valores [3] > valores[5]:
    maior = valores[3]
if valores [4] > valores[3] and valores [4] > valores[5]:
    maior = valores[4]
if valores [5] > valores [3] and valores [5] > valores[4]:
    maior = valores[5]

soma = valores[2] + valores[5] + valores[8]

print('-=' * 20)

for space in range(0,9):
    print(f'[ {valores[space]} ]', end =' ')
    if space == 2:
        print(end = '\n')
    if space == 5:
        print(end = '\n')
print()
print('-=' * 20)
print(f'A soma dos valores pares é {pares}')
print(f'A soma dos valores da terceira coluna é {soma}.')
print(f'O maior valor da segunda linha é {maior}')
