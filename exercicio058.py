from random import randint 

cont = 1
jogador = int(input("JOGADA USUÁRIO: "))

pc = randint(0, 10)
print(f'JOGADA COMPUTADOR: {pc}')


print(f'O jogador escolheu {jogador} e o computador escolheu {pc}')

while jogador != pc:
    print('TENTE NOVAMENTE')
    cont += 1
    jogador = int(input("JOGADA USUÁRIO: "))
    pc = randint(0, 10)
    print(f'O jogador escolheu {jogador} e o computador escolheu {pc}')
    if jogador == pc:
        print('VOCÊ GANHOU!!')
        print(f'Foram necessárias {cont} jogadas')
