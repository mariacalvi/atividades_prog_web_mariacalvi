# Faça um programa que peça ao usuário para digitar uma lista de números e que, em
# seguida, retorne uma nova lista com os quadrados de cada número. Use mapeamento.
numbers = input("Enter a space-separed numbers list: ")

numbers_list = list(map(float, numbers.split()))

squares = map(lambda x: x**2, numbers_list)

print(list(squares))