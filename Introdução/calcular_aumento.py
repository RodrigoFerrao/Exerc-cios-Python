"""
13) Faça um algoritmo que leia o salário de um funcionário, calcule e mostre o
seu novo salário, com 15% de aumento.
"""

# Ler salário do funcionário
# Calcular aumento
# Imprimir aumento

salario = float(input('Digite o salário do funcionário que irá receber o aumento:'))
aumento = float(input('Digite a porcentagem do aumento do funcionario:'))
calculoaumento = (salario * aumento / 100)
salarionovo = salario + calculoaumento
print(f'O salário do funcionario após o aumento de {aumento}% será {salarionovo}')
