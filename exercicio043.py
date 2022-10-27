peso = float(input('Insira seu peso: '))
altura = float(input('Insira sua altura: '))
imc = peso / altura**2
if imc < 18.5:
    print('Seu IMC deu {:.2f}. Você está abaixo do peso.' . format(imc))
elif  18 <= imc <= 25:
    print('Seu IMC deu {:.2f}. Você está no peso ideal.' .format(imc))
elif 25 <= imc <= 30:
    print('Seu IMC deu {:.2f}. Você está no sobrepeso.' . format(imc))
elif 30 <= imc <= 40:
    print('Seu IMC deu {:.2f}. Você está com um quadro de obesidade.' . format(imc))
elif imc > 40:
    print('Seu IMC deu {:.2f}. Você está com um quadro de obesidade mórbida' . format(imc))