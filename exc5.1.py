# Use list comprehension para criar uma lista com as raízes quadradas dos números
# pares de 0 a 20.

numbers = list(range(0,21))
squared = [x**2 for x in numbers if x % 2 == 0 ]
print(squared)