"""
16) [DESAFIO] Escreva um programa para calcular a redução do tempo de vida de um
fumante. Pergunte a quantidade de cigarros fumados por dias e quantos anos ele
já fumou. Considere que um fumante perde 10 min de vida a cada cigarro. Calcule
quantos dias de vida um fumante perderá e exiba o total em dias.
"""

# Ler quantidade de cigarros fumados diariamente
# Ler quantidade de tempo de uso do cigarro (em anos)
# Calcular quantos dias de vida o fumante perderá levando em consideração que o cigarro perde 10 minutos de vida
# Imprimir quantos dias de vida serão perdidos

print('Digite a quantidade de cigarros fumados por dia e a quantos anos fuma para realizar o calculo')
cigarro_por_dia = int(input('Quantos cigarros você fuma por dia?'))
anos_fuma = int(input('Tem quantos anos que você fuma?'))
reduzido_minutos = anos_fuma * 365 * cigarro_por_dia * 10
tempo_reduzido_dia = reduzido_minutos / 1440
print(f'Sua expectativa de vida diminuiu em  aproximadamente {int(tempo_reduzido_dia)} dias por conta do cigarro :(')
