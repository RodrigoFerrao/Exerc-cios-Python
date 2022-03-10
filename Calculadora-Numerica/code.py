# Calculadora númerica em Python
# OBS: a calculadora se encontra em um nível muito básico atualmente, tenho planos de melhorias no futuro.

escolha = '0'
menos = multiplicacao = divisao = soma = 0
while escolha not in range(0, 6):
    print("Olá, seja bem vindo a calculadora python, por favor escolha a opção desejada")
    print("1 - Adição")
    print("2 - Subratação")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Sair da calculadora")
    escolha = int(input("Escolha a opção desejada\n"))
    if escolha not in range(0, 6):
        print("Por favor escolha uma opção válida")
    if escolha == 1:
        print("Você escolheu 1- Adição")
        qtd1 = int(input("Escolha a quantidade de números que deseje somar\n"))
        for i in range(1, qtd1+1):
            num = float(input(f"Digite o numero {i} de {qtd1} que deseje adicionar a soma\n"))
            soma += num
        print(f"Você digitou {qtd1} números e a soma deles é {soma}")
    if escolha == 2:
        print("Você escolheu 2- Subtração")
        sub1 = float(input("Escolha o primeiro número da subtração\n"))
        sub2 = float(input("escolha o segundo número da subratração\n"))
        menos += sub1 - sub2
        print(f"VocÊ digitou {sub1} e {sub2} e o resultado da subtração deles é {menos}")
    if escolha == 3:
        print("Você escolheu 3 - Multiplicação")
        multi1 = float(input("Escolha o primeiro número a ser multiplicado\n"))
        multi2 = float(input("Escolha o segundo número a ser multiplicado\n"))
        multiplicacao += multi1 * multi2
        print(f"Você digitou {multi1} e {multi2} e o resultado da multiplicação deles é {multiplicacao}")
    if escolha == 4:
        print("Você escolheu divisão")
        divi1 = float(input("Escolha o número que será dividido\n"))
        divi2 = float(input("Escolha o número pelo qual ele será dividido\n"))
        divisao += divi1 / divi2''
        print(f"Você digitou {divi1} e {divi2} o resultado da divisão entre eles é {divisao}")

