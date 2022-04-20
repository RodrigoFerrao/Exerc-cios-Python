"""
7) Crie um algoritmo que leia um número real e mostre na tela o seu dobro e a
sua terça parte.
Ex:
Digite um número: 3.5
O dobro de 3.5 é 7.0
A terça parte de 3.5 é 1.16666
"""
num = float(input('Digite o número que deseje saber o dobro e a terça parte do mesmo\n'))
terca = num / 3
dobro = num * 2
print(f'O número escolhido foi {num}\n a terça parte é {terca}\n o dobro é {dobro}\n')
