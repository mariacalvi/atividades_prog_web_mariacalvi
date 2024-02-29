# Calcule o fatorial de um número digitado pelo usuário.

numero = int(input("Digite um número: "))

fatorial = 1

if numero < 0:
    print ("Não existe fatorial para número negativo")
elif numero == 0:
    print("O fatorial é 1.")
else:
    while numero > 0:
        fatorial = fatorial * numero
        numero -= 1 # O valor de numero é decrementado em 1 a cada iteração do loop.
    print(fatorial)