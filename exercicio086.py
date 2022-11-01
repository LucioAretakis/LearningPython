valores = []
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
print('-=' * 20)
for space in range(0,9):
    print(f'[ {valores[space]} ]', end =' ')
    if space == 2:
        print(end = '\n')
    if space == 5:
        print(end = '\n')
 
