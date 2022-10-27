primeiro = int(input("INSIRA O PRIMEIRO TERMO: "))
razao = int(input("INSIRA A RAZÃO DA SUA PA: "))
decimo = primeiro + (10-1) * razao
resp = ' '
while primeiro + razao <= decimo + razao:
   print(f'{primeiro}', end=' -> ')
   primeiro += razao
while True:
   cont = 0
   resp = int(input('\n'"QUANTOS TERMOS A MAIS DEVEM SER MOSTRADOS? "))
   if resp == 0:
      break
   while cont < resp:
      print(f'{primeiro}', end=' -> ')
      primeiro += razao
      cont += 1

print("OBRIGADO POR USAR O PROGRAMA!!")
