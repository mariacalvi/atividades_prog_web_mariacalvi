# Escreva um programa que verifique se um número digitado pelo usuário é positivo,
# negativo ou zero. 

numero = int(input("Escreva um número:"))

if numero > 0:
    print ("O número é positivo!")
elif numero < 0:
    print ("O número é negativo")
else:
    print ("O número é neutro!")