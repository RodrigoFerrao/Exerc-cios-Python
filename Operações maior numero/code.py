# Exercicio de fixação sobre operações enquanto utilizo o While

resposta = "S"
soma = quant = media = maior = menor = 0
while resposta == "S":
    numero = int(input("Digite um número\n"))
    soma += numero
    quant += 1
    if quant == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    resposta = str(input("Quer continuar? [S/N]\n")).upper().strip()[0]
media = soma / quant
print(f"Terminou, sua média é {media}, você digitou {quant} numeros, o maior deles foi {maior} e o menor {menor}")

