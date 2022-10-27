valores = []
while True:

    num = int(input('Digite um valor para ser adicionado a lista: '))
    if num not in valores:
        valores.append(num)
    resp = input('deseja digitar mais valores? ').strip().upper()[0]
    while resp not in 'SN':
        resp = input('resposta inválidade, responda com sim ou não: ').upper()[0]
    if resp in 'Nn':
        break
print(valores)
print(f'A sua lista em ordem crescente é {sorted(valores)}')