# Faça um programa que "sorteie" uma ordem

from random import shuffle

n1 = str(input('Primeiro nome: '))
n2 = str(input('Segundo nome: '))
n3 = str(input('Terceiro nome: '))
n4 = str(input('Quarto nome: '))
# n5 = str(input('Quinto nome: '))

nomes = [n1, n2, n3, n4]
shuffle(nomes)
print(f'O nome escolhido foi {nomes}')