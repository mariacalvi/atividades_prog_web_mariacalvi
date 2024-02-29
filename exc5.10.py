# Faça um programa que peça ao usuário para digitar uma lista de palavras e que, em
# seguida, retorne uma nova lista com os comprimentos de cada palavra.
words_list = input("Enter a space separated words list: ")
words = words_list.split()

words_length = list(map(lambda x: len(x), words))
print(f"{words_length}")