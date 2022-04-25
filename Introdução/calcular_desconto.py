"""
12) Crie um programa que leia o preço de um produto, calcule e mostre o seu
PREÇO PROMOCIONAL, com 5% de desconto.
"""

# Ler o preço do produto
# Calcular desconto (na questão definido como 5%)
# Imprimir o preço e o desconto

preco = float(input('Digite o preço do produto para calcular o desconto de 5%:'))
desconto = preco * 0.95
print(f'O item custa {preco} e após a aplicação de 5% irá custar {desconto}')
