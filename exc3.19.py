# Verificar se uma palavra digitada pelo usuário é um palíndromo. Se for, imprimir, ao
# final, “A palavra é um palíndromo”. Se não for, imprimir “A palavra não é um palíndromo”

palavra = input("Digite uma palavra:")

palindromo = palavra[:: -1]
if palavra == palindromo:
    print (f"A palavra {palavra} é um palíndromo")
else:
    print (f"A palavra {palavra} não é um palíndromo")