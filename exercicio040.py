n1 = float(input('Nota da primeira prova: '))
n2=  float(input('Nota da segunda prova: '))
media = (n1+n2)/2
print('A média entre {:.1f} e {:.1f} é igual à {:.1f}.'.format(n1, n2, media))
if media >= 7.0:
    print('PARABÉNS VOCÊ FOI APROVADO!')
elif 7 > media > 5:
    print('VOCÊ ESTÁ NA RECUPERAÇÃO')
elif media < 5:
    print('INFELIZMENTE VOCÊ FOI REPROVADO')