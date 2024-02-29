# Escreva um programa que verifique se um número inteiro digitado pelo usuário é
# divisível por outro número inteiro # digitado pelo usuário ou não.
numero_1 = int(input("Digite um número: "))
numero_2 = int(input("Digite outro número: "))

if numero_1 % numero_2 == 0 or numero_2 % numero_1 == 0 :
    print(f"O número é divisivel pelo outro")
else:
    print(f"O numero nao eh divisivel")

    