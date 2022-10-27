primeiro = int(input("INSIRA O PRIMEIRO TERMO: "))
razao = int(input("INSIRA A RAZÃO DA SUA PA: "))
decimo = primeiro + (10-1) * razao
while primeiro + razao <= decimo + razao:
   print(f'{primeiro}', end=' -> ')
   primeiro += razao
print("ACABOU!!!")