"""
17) Escreva um programa que pergunte a velocidade de um carro. Caso ultrapasse
80Km/h, exiba uma mensagem dizendo que o usuário foi multado. Nesse caso, exiba
o valor da multa, cobrando R$5 por cada Km acima da velocidade permitida.
"""

# Receber velocidade do carro
# Checar se ultrapassa 80km/h
# ^> Exibir mensagem de multa e valor da multa, 5 reais por km acima de 80km
# mandar mensagem falando que não foi multado

velocidade = float(input('Digite a velocidade do carro:'))
if velocidade > 80:
    multa = (velocidade - 80) * 5
    print(f'Você ultrapassou o limite em {velocidade - 80}km/h de velocidade e foi multado em R${multa}')
else:
    print('Continue respeitando os limites de velocidade')
    
