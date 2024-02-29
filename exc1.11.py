#  Peça ao usuário para digitar três números e calcule a fórmula de Bhaskara para
#  esses números.

primeiro_numero = int(input("Digite o primeiro número:")) # a
segundo_numero = int(input("Digite o segundo número:"))   # b
terceiro_numero = int(input("Digite o terceiro número:")) # c


import math
delta = segundo_numero**2 - 4*primeiro_numero*segundo_numero

if delta >= 0:
    x1 = (-segundo_numero + math.sqrt(delta)) / (2*primeiro_numero)
    x2 = (-segundo_numero - math.sqrt(delta)) / (2*primeiro_numero)
    print(f"As raízes reais são: x1 = {x1}, x2 = {x2}")
else:
    
    parte_real = -segundo_numero / (2*primeiro_numero)
    parte_imaginaria = math.sqrt(abs(delta)) / (2*primeiro_numero)
    raiz1 = complex(parte_real, parte_imaginaria)
    raiz2 = complex(parte_real, -parte_imaginaria)
    print(f"As raízes complexas são: Raiz 1 = {raiz1}, Raiz 2 = {raiz2}")

