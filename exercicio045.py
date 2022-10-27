from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Escolha sua jogada
[0] Pedra
[1] Papel
[2] Tesoura''')
jogador = int(input('Escolha sua jogada: '))
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO!!!')
sleep(0.3)
print('-=' * 11)
print('Você escolheu {}.' .format(itens[jogador]))
print('O computador escolheu {}.' .format(itens[computador]))
print('-=' * 11)
if computador == 0:
    if jogador == 0:
        print('A PARTIDA DEU EMPATE')
    elif jogador == 1:
        print('O JOGADOR VENCEU A PARTIDA')
    elif jogador == 2:
        print('O COMPUTADOR VENCEU A PARTIDA')
    else:
        print('JOGADA INVÁLIDA')
elif computador == 1:
    if jogador == 0:
        print('O COMPUTADOR VENCEU A PARTIDA')
    elif jogador == 1:
        print('A PARTIDA DEU EMPATE!')
    elif jogador == 2:
        print('O JOGADOR VENCEU A PARTIDA')
    else:
        print('JOGADA INVÁLIDA')
elif computador == 2:
    if jogador == 0:
        print('O JOGADOR VENCEU A PARTIDA')
    elif jogador == 1:
        print('O COMPUTADOR VENCEU A PARTIDA')
    elif jogador == 2:
        print('A PARTIDA DEU EMPATE')
    else:
        print('JOGADA INVÁLIDA')
