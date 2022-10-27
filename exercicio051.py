primeiro = int(input('Insira o primeiro termo da sua progressão aritmética: '))
razao = int(input('Insira a razão da sua PA: '))
decimo = primeiro + (10-1) * razao
for c in range(primeiro, decimo + razao , razao):
    print('{}'. format(c), end=' -> ' )
print('acabou!!')