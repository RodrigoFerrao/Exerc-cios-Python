"""
3) Crie um programa que leia o nome e o salário de um funcionário, mostrando no
final uma mensagem.
Ex:
Nome do Funcionário: Maria do Carmo
Salário: 1850,45
O funcionário Maria do Carmo tem um salário de R$1850,45 em Junho.
"""

nome = input("Olá, por favor digite o seu primeiro e último nome\n").title()
print(f"Seja bem-vindo {nome}, por favor digite o seu salário")
salario = float(input())
print(f"Funcionário {nome} recebe um salário de R${salario} mensalmente\n")
