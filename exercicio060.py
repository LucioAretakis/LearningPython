from math import factorial
n = int(input("NÚMERO : "))
c = n
total = factorial(n)
while c > 0:
    print(f'{c}', end = '')
    print(' x ' if c > 1 else ' = ', end = '')
    c -= 1
print(total)

