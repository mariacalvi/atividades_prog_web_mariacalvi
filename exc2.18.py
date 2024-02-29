# Escreva um programa que pergunte ao usuário sua idade e exiba uma mensagem
# de “Você é jovem” se a idade for menor do que 30, “Você é adulto” se a idade estiver entre 30 e 60,
# ou “Você é idoso” caso contrário.

idade = int(input("Digite sua idade: "))

if idade < 30 :
    print("Você é jovem")
elif idade >= 30 and idade <= 60 :
    print("Você é adulto")
else:
    print("Você é idoso")