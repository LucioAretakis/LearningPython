a = []
b = []
c = []

while True:
    a.append(int(input('insira um valor na lista: ')))
    resp = input('Você deseja continuar? ').strip().upper()[0]
    while resp not in 'SN':
        resp = input('Resposta inválida, responda com S ou N').strip().upper()[0]
    if resp in 'N':
        break
for v in a:
    if v % 2 == 0:
        b.append(v)
for v in a:
    if v % 2 != 0:
        c.append(v)
print('-=' * 20)
print(f'LISTA : {a}')
print(f'números pares presentes na lista {b}')
print(f'números impares presentes na lista {c}')

