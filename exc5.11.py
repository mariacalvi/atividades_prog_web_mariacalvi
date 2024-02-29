# Faça um programa que peça ao usuário para digitar uma lista de números e que, em
# seguida, retorna uma nova lista apenas com os números pares. 
numbers_list = input("Enter with a space-separated numbers list: ")
numbers = list(map(int, numbers_list.split()))

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)
