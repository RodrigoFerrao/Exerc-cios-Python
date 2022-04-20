"""
5) Faça um programa que leia as duas notas de um aluno em uma matéria e mostre
na tela a sua média na disciplina.
Ex:
Nota 1: 4.5
Nota 2: 8.5
A média entre 4.5 e 8.5 é igual a 6.5
"""

notacalc = 0
nome = input("Olá, seja bem-vindo aluno, por favor se identifique com o seu primeiro e último nome\n").title()
print(f"Seja bem-vindo {nome}, por favor digite as suas 2 notas para saber sua média")
nota1 = float(input('Digite sua primeira nota\n'))
nota2 = float(input('Digite sua segunda nota\n'))
media = (nota1 + nota2) / 2
print(f"{nome}, sua primeira nota foi {nota1} e sua segunda nota {nota2} sua média é {media}")
