# Faça um programa que sorteie um nome dentro de uma lista.

from random import choice

n1 = str(input('Primeiro nome: '))
n2 = str(input('Segundo nome: '))
n3 = str(input('Terceiro nome: '))
# n4 = str(input('Quarto nome: '))
# n5 = str(input('Quinto nome: '))

nomes = [n1, n2, n3]
print(f'O nome escolhido foi {choice(nomes)}')