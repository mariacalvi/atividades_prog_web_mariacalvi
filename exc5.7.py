# Crie um dicionário com nomes e notas de alunos digitados pelo usuário, usando os
# nomes dos alunos como chave e as notas como valor. Em seguida, use dict comprehension para
# criar um dicionário com os alunos e suas notas arredondadas para o número inteiro mais próximo
# da nota do aluno.

students = ['Harry', 'Julia', 'Hunter']
grades = [4.7, 3.9, 2.7]

students_grade = {name: grade for name, grade in zip(students, grades)}

rounded_grades = {name: round(grade) for name, grade in students_grade.items()}

print("Rounded grades dicionary: ")
print(rounded_grades)