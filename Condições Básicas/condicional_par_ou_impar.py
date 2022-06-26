"""
20) Desenvolva um programa que leia um número inteiro e mostre se ele é PAR ou
ÍMPAR.
"""
# Receber um número do usuário
# Verificar se o número é par ou impar
# Imprimir resultado da verificação

numero = int(input('Digite o número que deseja saber se é par ou ímpar:'))
par_ou_impar = numero % 2
if par_ou_impar == 0:
    print(f'O numéro {numero} é Par')
else:
    print(f'O número {numero} é ímpar')
