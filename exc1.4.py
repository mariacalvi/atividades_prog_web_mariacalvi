# Peça ao usuário para digitar seu peso e altura, calcule o índice de massa corporal
# (IMC) e imprima o resultado.

peso = float(input("Digite o seu peso (kg):"))
altura = float(input("Digite a sua altura(m):"))

imc = peso / (altura ** 2)
print(f"Seu IMC é {imc}")