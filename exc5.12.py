# Escreva um programa que leia duas listas, uma com as chaves e outra com os
# valores, e retorna um dicionário.
 
first_list = [1, 2, 3, 4]
second_list = [100, 200, 300, 400]

dictionary = dict(zip(first_list, second_list))
print(dictionary)