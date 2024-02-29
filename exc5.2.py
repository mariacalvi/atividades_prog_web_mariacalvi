# Use list comprehension para criar uma lista com as palavras que contêm a letra “a”
# em uma frase digitada pelo usuário, substituindo a letra por “o”.

sentence = input("Enter a sentence: ")
words  = sentence.split()

words_with_a =[w for w in words if "a" in w]
replaced_by_o = [w.replace("a", "o") for w in words_with_a]
print(replaced_by_o)