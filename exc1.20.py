# Peça ao usuário para digitar o valor da medida de um ângulo em radianos e calcule
# o valor desse ângulo em graus

medida_radianos = float(input("Digite o valor da medida de um ângulo (radianos): "))

graus =  medida_radianos * (180/3.14)

print(f"O valor desse ângulo em graus equivale a {graus}")