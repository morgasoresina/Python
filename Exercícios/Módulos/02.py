#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

from math import hypot
cOp = float(input('Comprimento do cateto oposto: '))
cAdj = float(input('Comprimento do cateto adjacente: '))
print(f'A hipotenusa é {hypot(cOp, cAdj):.2f}')