#  Use dict comprehension para criar um dicionário com as raízes quadradas dos
# números de 1 a 10. Utilize os números como chave e as raízes quadradas como valor.
import math

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = {x: math.sqrt(x) for x in numbers}
print(squares)

# squares = {x: x ** 0.5 for x in range(1, 11)}