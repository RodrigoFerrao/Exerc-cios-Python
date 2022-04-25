"""
11) Desenvolva uma lógica que leia os valores de A, B e C de uma equação do
segundo grau e mostre o valor de Delta.
"""

# Ler os valores de A, B e C de uma equação de segundo grau
# Realizar o calculo de Delta (-b * 4 * a * c)
# Imprimir o resultado do calculo de Delta

print('Olá, para fazer o calculo de delta por favor insira os valores da equação de segundo grau')
a = float(input('Valor de A:'))
b = float(input('Valor de B:'))
c = float(input('Valor de C:'))
delta = b**2 - 4 * a * c
print(f'O valor de delta é {delta}')
