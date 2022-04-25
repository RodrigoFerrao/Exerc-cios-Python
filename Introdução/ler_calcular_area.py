"""
10) Faça um algoritmo que leia a largura e altura de uma parede, calcule e
mostre a área a ser pintada e a quantidade de tinta necessária para o serviço,
sabendo que cada litro de tinta pinta uma área de 2metros quadrados.
"""

# Ler altura e largura
# Calcular e mostrar a area a ser pintada juntamente com a quantidade de tinta (1 litro para 2 metros)

altura = float(input('Digite a altura em metros do muro a ser pintado:'))
largura = float(input('Digite a largura em metros do muro a ser pintado:'))
area = altura * largura
pintura = area / 2
print(f'Para pintar uma area de {area} metros quadrados, serão necessários {pintura} litros de tinta
