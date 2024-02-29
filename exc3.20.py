# Calcular o fatorial de todos os números de 1 a n, onde n é digitado pelo usuário.
# Imprima o resultado para cada número.

numero = int(input("Digite um número: "))
fatorial = 1

for i in range(1, numero + 1):
 fatorial *= i
 print("O fatorial de", i , "é", fatorial)