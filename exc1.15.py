# Peça ao usuário para digitar a distância e a velocidade inicial de um objeto em queda
# livre e calcule o tempo que ele leva para atingir o solo, desconsiderando a resistência do ar
import math

distancia = float(input("Digite a distância percorrida pelo objeto (em metros): "))
velocidade_inicial = float(input("Digite a velocidade inicial do objeto (em metros por segundo): "))
gravidade = 9.8

a = 0.5 * gravidade
b = velocidade_inicial
c = -distancia

delta = b**2 - 4*a*c
if delta >= 0:
    tempo1 = (-b + math.sqrt(delta)) / (2*a)
    tempo2 = (-b - math.sqrt(delta)) / (2*a)
    print(f"O objeto leva {max(tempo1, tempo2)}s para atingir o solo")
else:
    print("O objeto não atinge o solo")
