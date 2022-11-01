par = list()
impar = list()
valores = [par, impar]
for c in range(0,7):
    num = int(input('Insira seus valores: '))
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)

print(sorted(par))
print(sorted(impar)) 
