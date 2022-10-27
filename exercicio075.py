num = (int(input("insira o número: ")),
    int(input("insira outro número: ")),
    int(input("insira mais um: ")),
    int(input("insira o último número: ")))
if num.count(9) > 1:
    print(f'O número nove aparece {num.count(9)} vezes')
else:
    print('O número nove não aparece nenhuma vez')
if 3 in num:
    print(f'O número três aparece pela primeira vez na {num.index(3) + 1}ª posição')
else:
    print(f'O número três não aparece na tupla.')
print('Números pares presentes na tupla: ', end = '')
for n in num:
    if n % 2 ==0:
        print(f'{n} ', end = '')
 

