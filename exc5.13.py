#  Escreva um programa que leia duas listas de mesmo tamanho e retorna uma nova
# lista com a média dos elementos correspondentes.
list1 = list(map(float, input("Enter with the first list: ").split()))
list2 = list(map(float, input("Enter with the second list: ").split()))

result_list = [(x + y) / 2 for x, y in zip(list1, list2)]

print(f"Result list: {result_list}")

