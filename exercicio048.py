n = 0
soma = 0
for c in range(1, 500+1):
    if c % 2 != 0 and c % 3 == 0:
        print(c)
        n += 1
        soma += c
print('O número total de números impares e múltiplos de 3 foi de {}, e a soma deles deu {}.'.format(n, soma))