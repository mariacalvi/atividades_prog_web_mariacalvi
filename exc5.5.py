# Crie um dicionário com nomes e notas de alunos digitados pelo usuário, usando os
# nomes dos alunos como chave e as notas como valor. Em seguida, use dict comprehension para
# criar um dicionário com os alunos com nota igual ou superior a 7.

names = ['Luke', 'Anne', 'Mary', 'Harry']
grades = [5, 8, 9, 10]

students_grade = {name: grade for name, grade in zip(names, grades)}

grades_equal_above_seven = {name: grade for name, grade in students_grade.items() if grade >=7}

print(grades_equal_above_seven)