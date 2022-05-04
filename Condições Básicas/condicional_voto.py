"""
18) Faça um programa que leia o ano de nascimento de uma pessoa, calcule a idade
dela e depois mostre se ela pode ou não votar.
"""

# ler ano de nascimento
# calcular idade através do ano de nascimento
# ^> imprimir mensagem avisando que ela pode votar caso idade >= 16
# avisar que ela não pode votar

anonasc = int(input('Digite o seu ano de nascimento:'))
idade = 2022 - anonasc
pode_votar = idade >= 16
if pode_votar:
    print('Você pode votar, pois já possui a idade minima de 16 anos!')
else:
    print('O voto requer uma idade minima de 16 anos, você ainda não pode votar.')
    
