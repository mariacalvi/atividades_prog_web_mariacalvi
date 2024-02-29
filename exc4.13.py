# Crie um programa que peça ao usuário para digitar uma frase, divida-a em palavras, remova todos os espaços em branco desnecessários dessas palavras, e componha a frase
# novamente com apenas 1 espaço entre as palavras.

frase = input("Digite uma frase: ")
palavras = frase.split() 

frase_sem_espacos = ' '.join(palavra.strip() for palavra in palavras)

print(f"A frase sem espaços desnecessários: {frase_sem_espacos}")