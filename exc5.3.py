# Use list comprehension para criar uma lista com o quadrado dos números pares entre
# 0 e 10.
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = [x**2 for x in numbers if x % 2 == 0]
print(squares) 