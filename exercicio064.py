cont = soma = 0
while True:
    n = int(input("NÚMERO: "))
    if n == 999:
        break
    cont += 1
    soma += n
print(f'Foram inseridos {cont} números e a soma deles foi {soma}')