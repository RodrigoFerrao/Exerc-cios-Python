"""
15) Crie um programa que leia o número de dias trabalhados em um mês e mostre o
salário de um funcionário, sabendo que ele trabalha 8 horas por dia e ganha R$25
por hora trabalhada.
"""

# Ler o numero de dias trabalhados
# Calcular dias trabalhados * ganho por hora
# Imprimir salário mensal

print('Para fazer o seu calculo de salário digite a quantidade de dias trabalhadas no mês')
diast = int(input('Digite a quantidade de dias trabalhados:'))
salario = diast * (25 * 8)
print(f'Você trabalhou por {diast} dias, seu salário é de R${salario}')
