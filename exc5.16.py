# Escreva um programa que leia uma lista de números e inverta a ordem dos elementos
# de índices pares.
numbers = list(map(float, input("Enter with an numbers list: ").split()))

inverted_numbers = numbers[::-2]

print("Inverted even numbers:", inverted_numbers)
