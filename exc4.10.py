# Crie um programa que peça ao usuário para digitar uma frase e que, em seguida,
# extraia todos os artigos da frase digitada e mostre-a sem os artigos.

frase = input("Digite uma frase: ")
artigos = ["o", "a", "os", "as", "um", "uma", "uns", "umas"]

palavras = frase.split()
artigos_na_frase = [palavra for palavra in palavras if palavra.lower() in artigos]

palavras_sem_artigos = [palavra for palavra in palavras if palavra.lower() not in artigos]

print("Artigos encontrados na frase:", artigos_na_frase)

nova_frase = ' '.join(palavras_sem_artigos)
print("Frase sem artigos:", nova_frase)
