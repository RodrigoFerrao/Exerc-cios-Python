"""
14) A locadora de carros precisa da sua ajuda para cobrar seus serviços. Escreva
um programa que pergunte a quantidade de Km percorridos por um carro alugado e a
quantidade de dias pelos quais ele foi alugado. Calcule o preço total a pagar,
sabendo que o carro custa R$90 por dia e R$0,20 por Km rodado.
"""

# Ler quantidade de KM e quantidade de dias de aluguel
# Calcular preço do aluguel
# R$ 90 por dia e R$ 0,20 por KM rodado

print('Para calcular o total a pagar, digite a quantidade de dias alugados e KM rodados')
dias = int(input('Dias alugados:'))
KM = float(input('KMs rodados:'))
preco = (dias * 90) + (KM * 0.20)
print(f'Você alugou o carro por {dias} dias, e rodou por {KM}km o total a pagar é R${preco}')
