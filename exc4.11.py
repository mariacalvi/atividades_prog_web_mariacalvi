# Crie um programa que peça ao usuário para digitar uma frase e que, em seguida,
# fatie a frase em substrings de 6 caracteres e mostre-as uma por linha
frase = input("Digite uma frase:")

substrings = [frase[i:i+6] for i in range(0, len(frase), 6)]

for substring in substrings:
    print(substring)
