# Escreva um programa que peça ao usuário para digitar 5 números inteiros. O
# programa deve exibir uma mensagem informando se todos os números digitados são pares ou se
# há pelo menos um número ímpar.


numero1 = int(input("Digite o primeiro número inteiro: "))
numero2 = int(input("Digite o segundo número inteiro: "))
numero3 = int(input("Digite o terceiro número inteiro: "))
numero4 = int(input("Digite o quarto número inteiro: "))
numero5 = int(input("Digite o quinto número inteiro: "))

impar = any(numero % 2 != 0 for numero in [numero1, numero2, numero3, numero4, numero5])

if impar:
    print("Há pelo menos um número ímpar")
else:
    print("Todos números digitados são pares")

## COM ESTRUTURA DE REPETIÇÂO

# numeros = []
# for i in range(5):
#     numero = int(input(f"Digite o {i+1}º número inteiro: "))
#    numeros.append(numero)

# todos_pares = all(num % 2 == 0 for num in numeros)

# if todos_pares:
#     print("Todos os números digitados são pares.")
# else:
#     print("Há pelo menos um número ímpar entre os digitados.")
