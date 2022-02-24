# Exercicio de fixação - Calculadora de IMC

Peso = float(input("Digite o seu peso\n"))
Altura = float(input("Digite a sua altura\n"))
IMC = Peso / (Altura ** 2)
print(f"Seu Peso é {Peso} sua altura é {Altura} e seu IMC é {IMC}")
if IMC < 18.5:
    print("Você está abaixo do peso")
elif 18.6 <= IMC <= 24.9:
    print("Você está Saudável")
elif 25 <= IMC <= 29.9:
    print("Você tem peso em excesso")
elif 30.0 <= IMC <= 34.9:
     print("Você tem obesidade de Grau I")
elif 35.0 <= IMC <= 39.9:
    print("Você tem obesidade de Grau II(Severa)")
elif IMC >= 40:
    print("Você tem Obesidade de Grau III(Mórbida)")
