# Peça ao usuário para digitar um número e calcule o seno, cosseno e tangente desse
# número. 

import math
numero = int(input("Digite um ângulo (em radiano):"))

seno = math.sin(numero)
cosseno = math.cos(numero)
tangente = math.tan(numero)

print (F"O seno equivale a: {seno}, o cosseno a:{cosseno}, e a tangente a:{tangente}")
