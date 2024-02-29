# Faça um programa que peça ao usuário para digitar uma lista de nomes e que, em
# seguida, retorne uma nova lista com os nomes em caixa alta. Use mapeamento. 
names_list = input("Enter a space separated names list: ")
names = names_list.split()

caps_lock_name = list(map(lambda x: x.upper(), names))
print((caps_lock_name))