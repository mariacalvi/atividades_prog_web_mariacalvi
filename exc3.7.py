# Calcule a média dos números digitados pelo usuário. O usuário deve digitar números
# até digitar um número negativo.


numeros = []

while True:
    entrada = input("Digite um número (um número negativo para sair): ")

    if float(entrada) < 0:
        break

    numeros.append(float(entrada))

if len(numeros) > 0:
    media = sum(numeros) / len(numeros)
    print(media)
# soma = 0
# contador = 0
# media = 0
# numero = float(input("Digite um número: "))
# while numero >= 0:
#  soma += numero
#  contador += 1
#  media = soma / contador
#  numero = float(input("Digite outro número: "))
# print("A média dos números é", media)
