# Encontre o segundo maior e o segundo menor número em uma lista de 10 números digitada pelo usuário.
numeros = [float(input(f"Digite o {i + 1}º número: ")) for i in range(10)]

if len(numeros) < 2:
    print("Digite ao menos 2 números")
else:
    numeros_ordenados = sorted(numeros)
    segundo_menor = numeros_ordenados[1]
    segundo_maior = numeros_ordenados[-2]

    print(f"{segundo_menor} é o segundo menor número")
    print(f"{segundo_maior} é o segundo maior número")
