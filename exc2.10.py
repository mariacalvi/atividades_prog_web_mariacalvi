# Escreva um programa que calcule a média de três números e exiba uma mensagem
# de “Aprovado” se a média for maior ou igual a 6, ou “Reprovado” caso contrário. Se a nota for 10,
# exiba também a mensagem “Parabéns”.

numero_1 = float(input("Digite o primeiro numero: "))
numero_2 = float(input("Digite o segundo numero: "))
numero_3 = float(input("Digite o terceiro numero: "))

media = ((numero_1 + numero_2 + numero_3) / 3)

if media < 6 :
    print (f"Reprovado")

elif (media >= 6) and (media < 10) :
    print(f"Aprovado !")

elif media == 10 :
    print (f"Parabéns ! Você está aprovado")
