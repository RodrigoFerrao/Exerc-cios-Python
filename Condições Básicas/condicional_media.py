"""
19) Crie um algoritmo que leia o nome e as duas notas de um aluno, calcule a sua
média e mostre na tela. No final, analise a média e mostre se o aluno teve ou
não um bom aproveitamento (se ficou acima da média 7.0).
"""

print('Bem-vindo a calculadora de médias, será necessário seu nome e suas dutas notas')
nome_aluno = input('Digite o seu nome:').title()
nota1 = float(input('Digite sua primeira média:'))
nota2 = float(input('Digite sua segunda média:'))
media_final = (nota1 + nota2) / 2
if media_final >= 7:
    print(f'{nome_aluno} sua média foi {media_final}\n Aprovado! Boas férias')
else:
    print(f'{nome_aluno} sua média foi {media_final}\nReprovado :( Estude mais!')
