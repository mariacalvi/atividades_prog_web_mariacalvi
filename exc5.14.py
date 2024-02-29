# Escreva um programa que leia duas listas de mesmo tamanho, uma com os nomes
# dos alunos e outra com as notas, e retorna uma lista com as tuplas (nome, nota) em ordem
# decrescente de nota.
# Solicita ao usuário para digitar duas listas de mesmo tamanho: uma com os nomes e outra com as notas
names = input("Enter with the students names: ").split()
grades = list(map(float, input("Enter with the students grades: ").split()))

names_and_grades = list(zip(names, grades))

sorted_decres = sorted(names_and_grades, key=lambda x: x[1], reverse=True)

print("Names and grades: ")
for name, grade in sorted_decres:
    print(f"{name}: {grade}")
