# Crie um programa que peça ao usuário para digitar uma frase e que, em seguida,
# mostre quantas vezes cada palavra aparece nessa frase.
frase = input("Digite uma frase: ")
palavras = frase.split()

for palavra in palavras:
    contagem = frase.count(palavra)
    print(f"A palavra '{palavra}' aparece {contagem} vezes na frase.")