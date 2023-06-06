# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
from math import trunc
numero = float(input('Insira o valor: '))
print(f'O valor {numero} possui {trunc(numero)} como porção inteira.')