sexo = input("SEXO [M/F]: ").lower().strip()

while sexo not in 'MmFf':
    print("OPÇÃO INVÁLIDA!")
    sexo = input("SEXO [M/F]: ")
if sexo in 'Mm':
    print("SEXO: MASCULINO")
elif sexo in 'Ff':
    print("SEXO: FEMININO")


