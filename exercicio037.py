num = int(input('Insira um número inteiro: '))
print('''Escolha uma das opções abaixo
[ 1 ] BINÁRIO 
[ 2 ] OCTAL
[ 3 ] HEXADECIMAL''')
opção = int(input('Sua opção foi: '))
if opção == 1:
    print('{} convertido para BINÁRIO é igual à {}.' .format(num, bin(num)[2:]))
elif opção == 2:
    print('{} convertido para OCTAL é igual à {}.' .format(num, oct(num)[2:]))
elif opção == 3:
    print('{} convertido para HEXADECIMAL é igual à {}'.format(num, hex(num)[2:]))
#[2:] serve para fatiar as duas primeiras strings
else:
    print('Opção inválida. Tente novamente.')