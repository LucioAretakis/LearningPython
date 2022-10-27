tup = ('agua', 'pao', 'queijo', 'presunto', 'mortadela')# cada palavra é uma lista, então você pode pegar elementos dela
for palavra in tup:
    print(f'\n Dentro da palavra {palavra.upper()} temos ', end= '',)
    for letra in palavra:
        if letra in 'aeiou':
            print(f'{letra} ', end='')

