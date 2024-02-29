# Crie um programa que peça ao usuário para digitar uma frase e que, em seguida,
# verifique quantas palavras terminam com a letra “o” e quantas terminam com a letra “a”. 

frase = input("Digite uma frase: ")

palavras = frase.split()
palavras_o = 0
palavras_a = 0

for palavra in palavras:
    if palavra.endswith('o'):
        palavras_o += 1
    elif palavra.endswith('a'):
        palavras_a += 1

print(f"Quantidade de palavras terminadas com 'o': {palavras_o}")
print(f"Quantidade de palavras terminadas com 'a': {palavras_a}")
