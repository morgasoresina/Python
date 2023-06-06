# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import radians, sin, cos, tan
ang = float(input('Qual o ângulo que deseja? '))
general = int(input('''
Você deseja calcular:
1 - SENO
2 - COSSENO
3 - TANGENTE
'''))

if (general == 1):
    seno = sin(radians(ang))
    print(f'O ângulo {ang} tem o seno de {seno:.2f}')
elif (general == 2):
    cosseno = cos(radians(ang))
    print(f'O ângulo {ang} tem o cosseno de {cosseno:.2f}')
elif (general == 3):
    tangente = tan(radians(ang))
    print(f'O ângulo {ang} tem a tangente de {tangente:.2f}')
else:
    print('Opção inválida!')