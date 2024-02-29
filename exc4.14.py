# Crie um programa que peça ao usuário para digitar uma frase e que, em seguida,
# mostre a posição inicial de cada palavra contida nessa frase.

frase = input("Digite uma frase: ")
palavras = frase.split()

for palavra in palavras:
    posicao = frase.find(palavra)
    print(f"A palavra '{palavra}' começa na posicao '{posicao}'")
