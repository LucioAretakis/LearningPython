while True:
    n1 = int(input("PRIMEIRO NÚMERO: "))
    n2 = int(input("SEGUNDO NÚMERO: "))
    print("""
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair
    """)
    resp = int(input("OPÇÃO: "))

    if resp == 1:
        op = n1 + n2
        print(op)
        break
    if resp == 2:
        op = n1 * n2
        print(op)
        break
    if resp == 3:
        if n1 > n2:
            print(f'{n1} é maior que {n2}')
        else:
            print(f'{n2} é maior que {n1}')
        break
    if resp == 5:

        break
print("OBRIGADO POR USAR NOSSO PROGRAMA!")