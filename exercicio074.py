from random import randint

alea = (randint(1,10), randint(1,10), randint(1,10), randint(1,10))
for n in alea:
    print(f'{n} ', end = '')
    if n == alea[3]:
        print(n)

print(f'O maior número foi {max(alea)}')
print(f'O menor número foi {min(alea)}')