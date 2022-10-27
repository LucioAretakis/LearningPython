somaidade = 0
mediaidade = 0
homemmaioridade = 0
nomevelho = ''
totmulher20 = 0
for pessoa in range(0,4):
    print('---------{}ª PESSOA--------'.format(pessoa + 1))
    nome = str(input('NOME: ')).strip()
    idade = int(input('IDADE: '))
    sexo = str(input('SEXO (M/F): ')).strip()
    somaidade += idade
    if pessoa == 1 and sexo in 'Mm':
        homemmaioridade = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > homemmaioridade:
        homemmaioridade = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
mediaidade = somaidade / 4
print('A média de idade das pessoas é de {} anos.'.format(mediaidade))
print('O nome do homem mais velho é {} e ele tem {} anos.' .format(nomevelho, homemmaioridade))
print('Ao todo são {} mulheres com menos de 20 anos.' .format(totmulher20))
