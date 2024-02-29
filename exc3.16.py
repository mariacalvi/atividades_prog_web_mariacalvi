# Encontre o maior e o menor número em uma lista de 10 números digitada pelo usuário.
# Inicializa uma lista vazia para armazenar os números
numeros = []

for _ in range(10):
    numero_digitado = float(input("Digite um número: "))
    numeros.append(numero_digitado)

maior_numero = max(numeros)
menor_numero = min(numeros)

print(f"{maior_numero} é o maior número digitado")
print(f"{menor_numero} é o menor número digitado")
