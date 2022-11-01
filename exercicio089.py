aluno = list()
while True:
    nome = input('nome: ')
    n1 = float(input('nota 1: '))
    n2 = float(input('nota 2: '))
    media = (n1 + n2) / 2
    dados = [nome, n1, n2, media]
    aluno.append(dados)

    resp = input('Você deseja continuar? ').strip().upper()[0]
    while resp not in 'SN':
        resp = input('Resposta inválida, responda com S ou N').strip().upper()[0]
    if resp in 'N':
        break


print('-=' * 10, 'BOLETIM', '-=' * 10)
for n, d in enumerate(aluno):
    print(f'{n} - {aluno[n][0]} ------------------- {aluno[n][3]}')

acesso = ' '
while acesso != 999:
    acesso = int(input('Você quer acessar as notas de qual aluno?(999 para interromper)'))
    for i, n in enumerate(aluno):
        if acesso == i:
            print(f'as notas de {aluno[i][0]} foram {aluno[i][1]} e {aluno[i][2]}.')

print('OBRIGADO POR USAR O PROGRAMA!!')


