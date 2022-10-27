num = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez')
while True:
    escolhido = int(input("DIGITE UM NÚMERO DE 0 A 10: "))
    if escolhido < 0 or escolhido > 10:
        print('tente novamente, escolha um número de 0 a 10: ' , end ='')
    else:
        print(f'O número escolhido foi {num[escolhido]} ')
        resp = input('Você deseja escolher outro número? ').upper()[0]
        if resp in 'Nn':
            break
print("OBRIGADOP POR USAR O PROGRAMA!")



