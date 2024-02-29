# Crie um programa que peça ao usuário para inserir um ângulo em graus e calcule o
# seno, cosseno e tangente desse ângulo.

import math

angulo = int(input("Digite um ângulo em graus: "))

cosseno = math.cos(angulo)
seno = math.sin(angulo)
tangente = math.tan(angulo)

print(f"O seno desse ângulo é {seno}, o cosseno é {cosseno} e sua tangente é {tangente} ")