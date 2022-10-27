import time
v1 = int(input('insira um valor: '))
v2 = int(input('insira outro valor: '))
print('Espera um pouquinho nós estamos comparando-os para você...')
time.sleep(1)
if v1 >v2:
    print('O primeiro valor é o maior.')
elif v1<v2:
    print('O segundo valor é o maior.')
else:
    print('Os valores são iguais.')
