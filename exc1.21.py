# Peça ao usuário para digitar o comprimento de dois lados de um triângulo retângulo
# e calcule o comprimento da hipotenusa.

import math

comprimento_lado_1 = float(input("Digite o valor de um lado do triângulo: "))
comprimento_lado_2 = float(input("Digite o valor de outro lado do triângulo: "))

comprimento_hipotenusa = math.sqrt(comprimento_lado_1**2 + comprimento_lado_2**2)

print(f"O comprimento da hipotenusa desse triângulo equivale á {comprimento_hipotenusa}")