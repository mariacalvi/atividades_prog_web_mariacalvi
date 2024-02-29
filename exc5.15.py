# Escreva um programa que leia uma lista de números e um número de referência e
# retorna a posição do primeiro elemento maior que o número de referência.
numbers = [15, 16, 12, 56, 20]
reference = 15

position = next((i+1 for i, num in enumerate(numbers) if num > reference), len(numbers)+1)
print(f"{position}°")
